from fastapi import APIRouter
from pydantic import BaseModel

from app.database import SessionLocal
from app.models import Resume
from app.services.matcher import calculate_match

router = APIRouter()


class MatchRequest(BaseModel):
    resume_id: int
    jd_text: str


@router.post("/match")
def match_resume(data: MatchRequest):

    db = SessionLocal()

    try:
        resume = db.query(Resume).filter(
            Resume.id == data.resume_id
        ).first()

        if not resume:
            return {
                "error": "Resume not found"
            }

        score = calculate_match(
            resume.resume_text,
            data.jd_text
        )

        resume.match_score = score
        db.commit()

        return {
            "resume_id": resume.id,
            "match_score": score,
            "status": "success"
        }

    finally:
        db.close()