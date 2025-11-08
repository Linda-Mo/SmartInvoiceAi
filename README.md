
# Project Title

A brief description of what this project does and who it's for

# SmartInvoice AI

**Automated Proof-of-Delivery Verification & Dummy USDC Payments Web App**

SmartInvoice AI is a web application designed to streamline proof-of-delivery verification. Users can upload invoices as text files or images, and the system will analyze the content for delivery confirmation keywords. Verified invoices trigger simulated USDC payments, which are tracked in a dynamic transaction history.

---

## Features

- Invoice Upload: Accepts `.txt`, `.md`, and image files (`.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`).  
- Automatic Verification: Detects delivery keywords such as "delivered", "signed", "received", "proof of delivery".  
- Dummy Payments: Processes simulated payments of **2 USDC** per verified invoice.  
- Dynamic UI Updates: Transaction history and payment amounts update automatically.  
- OCR Support: Extract text from images (requires Tesseract).  
- Transaction Details: Clickable rows in the history table show full transaction information.  
- Masked Wallets: Source and destination wallets are partially hidden for privacy.  
- Popups: Review, success, error, and transaction detail popups for user-friendly interaction.

---

## Tech Stack

- Backend: Python, FastAPI  
- Frontend: HTML, CSS, JavaScript  
- Template Engine: Jinja2  
- Payment Simulation: Circle API (dummy mode)  
- OCR: pytesseract and Pillow (optional)  
- Environment Management: Python `venv` and `.env` configuration

---

## Requirements

- Python 3.10+  
- pip package manager  
- Optional (for OCR support):  
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to PATH  
  - Python packages: `pillow`, `pytesseract`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smartinvoice-ai.git
cd smartinvoice-ai


2. Create a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt


4. Configure environment variables: Create a .env file:

CIRCLE_API_BASE=https://api.circle.com/v1
CIRCLE_API_KEY=your_api_key_here
SOURCE_WALLET_ID=source_wallet_id_here
DESTINATION_WALLET_ADDRESS=destination_wallet_address_here
PAYMENT_AMOUNT=2.0


For dummy payments, Circle API keys are optional; the app will simulate payments.

## Running the Application

Start the FastAPI server:

uvicorn main:app --reload


Open your browser and navigate to:

http://127.0.0.1:8000

## Using SmartInvoice AI

1. Upload an invoice: Click the file upload button and select a .txt file or image.

2. Review the invoice: A popup shows the selected file, source, destination, and payment amount.

3. Confirm payment: Click Confirm to process a simulated payment.

4. View results:

4.1 Success popup if verified.

4.2 Error popup if verification fails.

5. Transaction history: Scroll down to view all transactions. Click a row to see details like invoice number, confidence, reason, timestamp, and transaction ID.

## OCR and Image Uploads

1. SmartInvoice AI can read text from images using Tesseract OCR.

2. If Tesseract is not installed or not in PATH, image uploads will be skipped, and only text files will be processed.

3. Recommended Tesseract version: 5.x or higher.

4. Windows users may need to add Tesseract executable to system PATH.

## Transaction Simulation

1 .All verified invoices are processed as dummy 2 USDC payments.

2. Payment details are shown in a popup and stored in data/history.json.

3. Transaction history includes:

3.1 Invoice number

3.2 Status (Paid or Failed)

3.3 Confidence score

3.4 Verification reason

3.5 Timestamp

3.6 Transaction ID (dummy or real if API is connected)

## Error Handling

1. Unverified invoices or files without delivery keywords will trigger an error popup.

2. OCR failures will fall back gracefully to text extraction if possible.

3. Any unexpected server errors are logged and displayed in the UI.

## File Structure

smartinvoice-ai/
├── main.py                 # FastAPI backend
├── circle_client.py        # Payment simulation & Circle API integration
├── templates/
│   └── index.html          # Frontend HTML with popups and dynamic updates
├── static/
│   └── style.css           # CSS styles
├── data/                   # Uploaded files & transaction history
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # This file
'
## Dependencies
fastapi
jinja2
python-dotenv
requests
pillow
pytesseract
uvicorn

## License

MIT License © 2025
## Dependences
`
