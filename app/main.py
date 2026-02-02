from fastapi import FastAPI
from app.presentation.auth.auth_router import router as auth_router
from app.presentation.image.image_router import router as image_router

app = FastAPI(title="Gallery Backend")

app.include_router(auth_router)
app.include_router(image_router)
