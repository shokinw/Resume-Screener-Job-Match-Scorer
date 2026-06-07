from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from datetime import datetime
from app.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    skills = Column(Text)
    resume_text = Column(Text)
    match_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)