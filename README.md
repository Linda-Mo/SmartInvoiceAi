# SmartInvoice AI

![SmartInvoice Dashboard](dashboard.png)


![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)

Automated Proof-of-Delivery Verification and Dummy Payments Web Application.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [OCR and Image Uploads](#ocr-and-image-uploads)
7. [Transaction Simulation](#transaction-simulation)
8. [Error Handling](#error-handling)
9. [File Structure](#file-structure)
10. [Dependencies](#dependencies)
11. [License](#license)

## Overview
SmartInvoice AI allows users to upload invoices (text or image) to automatically verify delivery proof and process dummy payments (2 USDC). The application stores transaction history and provides a detailed review of each transaction.

## Features
- Upload `.txt` or image invoices
- OCR text extraction from images
- Automated delivery keyword analysis
- Dummy payment processing (simulated USDC transfer)
- Real-time UI updates for amounts
- Transaction history with detailed popup views
- Graceful error handling for failed verifications

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/smartinvoice-ai.git
cd smartinvoice-ai
```

2. **Create a virtual environment:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:** Create a `.env` file in the root directory:
```
CIRCLE_API_BASE=https://api.circle.com/v1
CIRCLE_API_KEY=your_api_key_here
SOURCE_WALLET_ID=source_wallet_id_here
DESTINATION_WALLET_ADDRESS=destination_wallet_address_here
PAYMENT_AMOUNT=2.0
```

> For dummy payments, Circle API keys are optional; the app will simulate payments.

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

## Usage

1. Upload an invoice: Click the file upload button and select a `.txt` file or image.
2. Review the invoice: A popup shows the selected file, source, destination, and payment amount.
3. Confirm payment: Click **Confirm** to process a simulated payment.
4. View results:
   - Success popup if verified
   - Error popup if verification fails
5. Transaction history: Scroll down to view all transactions. Click a row to see details like invoice number, confidence, reason, timestamp, and transaction ID.

## OCR and Image Uploads

- SmartInvoice AI can read text from images using Tesseract OCR.
- If Tesseract is not installed or not in PATH, image uploads will be skipped.
- Recommended Tesseract version: 5.x or higher.
- Windows users may need to add Tesseract executable to system PATH.

## Transaction Simulation

- All verified invoices are processed as dummy 2 USDC payments.
- Payment details are shown in a popup and stored in `data/history.json`.
- Transaction history includes:
  - Invoice number
  - Status (Paid or Failed)
  - Confidence score
  - Verification reason
  - Timestamp
  - Transaction ID (dummy or real if API is connected)

## Error Handling

- Unverified invoices or files without delivery keywords trigger an error popup.
- OCR failures fall back to text extraction if possible.
- Unexpected server errors are logged and displayed in the UI.

## File Structure
```
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
└── README.md               # Project documentation
```

## Dependencies
- fastapi
- jinja2
- python-dotenv
- requests
- pillow
- pytesseract
- uvicorn

## License

MIT License © 2025


