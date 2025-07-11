from fastapi import APIRouter, UploadFile, File
from .extractor import extract_text_from_pdf, extract_text_from_docx
import os

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/")
def root():
    return {"message": "TransformoDocs backend running"}

@router.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    ext = os.path.splitext(file.filename)[1].lower()

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(content)

    if ext == ".pdf":
        text = extract_text_from_pdf(content)
    elif ext == ".docx":
        text = extract_text_from_docx(content)
    else:
        text = "Unsupported file format. Only .pdf and .docx are supported."

    return {
        "filename": file.filename,
        "text": text[:3000]  # Limit response for preview
    }
