from fastapi import APIRouter, HTTPException
from app.presentation.auth.schemas import (
    RegisterRequest, LoginRequest, TokenResponse
)
from app.infrastructure.user.user_repository_impl import UserRepositoryImpl
from app.application.user.register_user import RegisterUser
from app.application.user.login_user import LoginUser

router = APIRouter(prefix="/auth", tags=["Auth"])

repo = UserRepositoryImpl()

@router.post("/register")
def register(data: RegisterRequest):
    try:
        RegisterUser(repo).execute(data.email, data.name, data.password)
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    try:
        token = LoginUser(repo).execute(data.email, data.password)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
