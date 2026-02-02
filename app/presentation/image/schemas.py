from pydantic import BaseModel

class ImageResponse(BaseModel):
    id: int
    filename: str
    title: str | None
