from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from app.presentation.dependencies import get_current_user
from app.infrastructure.image.image_repository_impl import ImageRepositoryImpl
from app.application.image.upload_image import UploadImage
from app.application.image.list_my_images import ListMyImages
from app.application.image.delete_image import DeleteImage
import uuid
import os

router = APIRouter(prefix="/images", tags=["Images"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

repo = ImageRepositoryImpl()

@router.post("/upload")
def upload_image(
    file: UploadFile = File(...),
    title: str | None = Form(None),
    user=Depends(get_current_user)
):
    filename = f"{uuid.uuid4()}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())

    image = UploadImage(repo).execute(
        owner_id=user.id,
        filename=filename,
        title=title
    )

    return {"id": image.id, "filename": image.filename}


@router.get("/me")
def my_images(user=Depends(get_current_user)):
    images = ListMyImages(repo).execute(user.id)
    return images


@router.delete("/{image_id}")
def delete_image(image_id: int, user=Depends(get_current_user)):
    try:
        DeleteImage(repo).execute(image_id, user.id)
        return {"message": "Image deleted"}
    except PermissionError:
        raise HTTPException(status_code=403, detail="Not allowed")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
