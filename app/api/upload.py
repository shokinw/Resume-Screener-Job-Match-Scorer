from fastapi import APIRouter, UploadFile, File
import os

from app.services.resume_parser import extract_text
from app.nlp import extract_skills
from app.database import SessionLocal
from app.models import Resume

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    db = SessionLocal()

    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        resume_text = extract_text(file_path)

        skills = extract_skills(resume_text)

        new_resume = Resume(
            filename=file.filename,
            skills=", ".join(skills),
            resume_text=resume_text
        )

        db.add(new_resume)
        db.commit()
        db.refresh(new_resume)

        return {
            "resume_id": new_resume.id,
            "filename": file.filename,
            "skills": skills,
            "resume_text": resume_text
        }

    except Exception as e:
        import traceback

        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }

    finally:
        db.close()