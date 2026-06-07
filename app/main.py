from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.api import upload, match

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resume Screener AI")  # ✅ FIRST define app

# ✅ THEN middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(upload.router)
app.include_router(match.router)