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
