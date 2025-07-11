# 📝 TransformoDocs

**TransformoDocs** is a FastAPI-based backend application that extracts readable text from uploaded `.pdf`, `.docx`, and `.txt` files. It is integrated with a React frontend and supports basic document parsing, ideal for text analysis, summarization, and other downstream tasks.

---

## 🚀 Features

- ✅ Upload `.pdf`, `.docx`, and `.txt` files
- 📄 Extracts machine-readable text (from OCR-friendly PDFs or DOCX/TXT)
- 🔁 React frontend with instant preview
- 🔐 CORS-enabled to work with frontend on `localhost:5173`

---

## 🧱 Tech Stack

| Layer     | Technology     |
|-----------|----------------|
| Backend   | FastAPI        |
| Frontend  | React (Vite)   |
| Parsing   | PyPDF2, docx2txt |
| Server    | Uvicorn        |

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/transformodocs-backend.git
cd transformodocs-backend

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

cd frontend
npm install
npm run dev
