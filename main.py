import io
import os
import json
from datetime import datetime
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Optional OCR
OCR_AVAILABLE = False
try:
    from PIL import Image
    import pytesseract
    OCR_AVAILABLE = True
except Exception:
    OCR_AVAILABLE = False

BASE_DIR = Path(__file__).parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "history.json"
if not HISTORY_FILE.exists():
    HISTORY_FILE.write_text("[]")

# Dummy wallets
SOURCE_WALLET_ID = "SRC1234567890"
DESTINATION_WALLET_ADDRESS = "DEST9876543210"
PAYMENT_AMOUNT = "2.0"

# Keywords to detect delivery confirmation
KEYWORDS = [
    "delivered", "signed", "received", "delivered and signed",
    "proof of delivery", "package received", "received and signed"
]

def analyze_text(text: str):
    t = (text or "").lower()
    hits = []
    score = 0
    for kw in KEYWORDS:
        if kw in t:
            hits.append(kw)
            score += 30
    if "signature" in t or "signed by" in t:
        score += 10
    score = min(100, score)
    verified = score >= 80
    reason = "Keywords: " + ", ".join(hits) if hits else "No delivery keywords detected."
    return score, verified, reason

def load_history():
    try:
        return json.loads(HISTORY_FILE.read_text())
    except Exception:
        return []

def save_history(record: dict):
    arr = load_history()
    arr.insert(0, record)
    HISTORY_FILE.write_text(json.dumps(arr, indent=2))

def mask_wallet(wid: str):
    return wid[:6] + "..." + wid[-4:]

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    history = load_history()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "history": history,
        "source_mask": mask_wallet(SOURCE_WALLET_ID),
        "dest_mask": mask_wallet(DESTINATION_WALLET_ADDRESS),
        "payment_amount": PAYMENT_AMOUNT,
        "popup": None,
        "error": None
    })

@app.get("/transaction/{invoice_id}")
def get_transaction(invoice_id: int):
    history = load_history()
    tx = next((item for item in history if item["invoice"] == invoice_id), None)
    if not tx:
        return JSONResponse({"error": "Transaction not found"}, status_code=404)
    return JSONResponse(tx)

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    upload_path = DATA_DIR / file.filename
    content_text = ""
    try:
        # save file
        with open(upload_path, "wb") as f:
            f.write(await file.read())

        # read text files
        fname = file.filename.lower()
        if fname.endswith((".txt", ".md")):
            content_text = upload_path.read_text(encoding="utf-8", errors="ignore")
        elif fname.endswith((".png", ".jpg", ".jpeg")) and OCR_AVAILABLE:
            img = Image.open(upload_path)
            content_text = pytesseract.image_to_string(img)

        confidence, verified, reason = analyze_text(content_text)
        invoice = len(load_history()) + 1

        if verified:
            status = "Paid"
            tx_id = f"TX-{invoice:04d}"
            error_msg = None
        else:
            status = "Failed"
            tx_id = "N/A"
            error_msg = "Invoice not verified as delivered. " + reason

        record = {
            "invoice": invoice,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status,
            "confidence": int(confidence),
            "reason": reason,
            "payment": {"tx_id": tx_id, "amount": PAYMENT_AMOUNT if status=="Paid" else "0"}
        }
        save_history(record)

        popup = record if status=="Paid" else None
        history = load_history()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "history": history,
            "popup": popup,
            "error": error_msg,
            "source_mask": mask_wallet(SOURCE_WALLET_ID),
            "dest_mask": mask_wallet(DESTINATION_WALLET_ADDRESS),
            "payment_amount": PAYMENT_AMOUNT
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "history": load_history(),
            "popup": None,
            "error": f"Server error: {str(e)}",
            "source_mask": mask_wallet(SOURCE_WALLET_ID),
            "dest_mask": mask_wallet(DESTINATION_WALLET_ADDRESS),
            "payment_amount": PAYMENT_AMOUNT
        })
