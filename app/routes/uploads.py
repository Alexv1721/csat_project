from fastapi import APIRouter, UploadFile, File
from app.services.s3_service import upload_file

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
def upload_image(file: UploadFile = File(...)):
    url = upload_file(file)
    return {"url": url}
