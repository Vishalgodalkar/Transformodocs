from PyPDF2 import PdfReader
import docx2txt
from io import BytesIO
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        # Step 1: Try text-based extraction
        pdf_reader = PdfReader(BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        # Step 2: If no text found, apply OCR
        if not text.strip():
            images = convert_from_bytes(file_bytes)
            for image in images:
                text += pytesseract.image_to_string(image)

        return text or "No readable text found in the document."

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_docx(file_bytes: bytes) -> str:
    try:
        from io import BytesIO
        file_stream = BytesIO(file_bytes)
        return docx2txt.process(file_stream)
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

def extract_text_from_txt(file_bytes: bytes) -> str:
    try:
        return file_bytes.decode("utf-8", errors="ignore")
    except Exception as e:
        return f"Error reading TXT: {str(e)}"
