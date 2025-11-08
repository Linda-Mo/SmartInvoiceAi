import os
import requests
from uuid import uuid4

CIRCLE_API_BASE = os.getenv("CIRCLE_API_BASE", "https://api.circle.com/v1")
CIRCLE_API_KEY = os.getenv("CIRCLE_API_KEY", "")
HEADERS = {
    "Authorization": f"Bearer {CIRCLE_API_KEY}",
    "Content-Type": "application/json"
}

def transfer_usdc(source_wallet_id: str, dest_address: str, amount: str, blockchain: str = "ARC-TESTNET", simulate: bool = False):
    """
    Calls Circle Web3 Services transfer endpoint.
    If simulate=True, returns a dummy transaction.
    """
    if simulate:
        return {
            "error": False,
            "data": {
                "id": str(uuid4()),
                "amount": amount,
                "currency": "USD",
                "source": source_wallet_id,
                "destination": dest_address,
                "status": "succeeded"
            }
        }

    url = f"{CIRCLE_API_BASE}/w3s/transactions/transfer"
    body = {
        "source": {"type": "wallet", "id": source_wallet_id},
        "destination": {"type": "blockchain_address", "address": dest_address, "chain": blockchain},
        "amount": {"amount": str(amount), "currency": "USD"},
        "idempotencyKey": str(uuid4())
    }

    try:
        resp = requests.post(url, json=body, headers=HEADERS, timeout=30)
        try:
            text = resp.text
        except Exception:
            text = "<no body>"
        if resp.status_code == 403:
            return {"error": True, "text": "403 Forbidden — check API key."}
        if resp.status_code >= 400:
            try:
                j = resp.json()
                msg = j.get("message") or j.get("error") or str(j)
            except Exception:
                msg = text
            return {"error": True, "text": f"HTTP {resp.status_code}: {msg}"}
        try:
            return {"error": False, "data": resp.json()}
        except Exception:
            return {"error": False, "data": {"raw_text": text}}
    except requests.exceptions.RequestException as e:
        return {"error": True, "text": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": True, "text": f"Unexpected error: {str(e)}"}
