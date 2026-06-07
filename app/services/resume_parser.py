import pdfplumber
from docx import Document
import os

def extract_text(file_path: str):

    ext = os.path.splitext(file_path)[1].lower()

    # -------- PDF --------
    if ext == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    # -------- DOCX --------
    elif ext == ".docx":
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    else:
        raise Exception("Unsupported file format. Upload PDF or DOCX only.")