from fastapi import FastAPI
from app.presentation.auth.auth_router import router as auth_router

app = FastAPI(title="Gallery Backend")

app.include_router(auth_router)
