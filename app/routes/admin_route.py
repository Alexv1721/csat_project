from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import schemas
from app.models import admin as admin_model
from app.services.auth_services import hash_password, verify_password, create_token

router = APIRouter(prefix="/admin")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(admin_data: schemas.AdminCreate, db: Session = Depends(get_db)):
    existing = db.query(admin_model.Admin).filter_by(email=admin_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email exists")

    new_admin = admin_model.Admin(
        name=admin_data.name,
        email=admin_data.email,
        password=hash_password(admin_data.password)
    )
    db.add(new_admin)
    db.commit()
    return {"message": "Admin registered"}

@router.post("/login")
def login(data: schemas.AdminLogin, db: Session = Depends(get_db)):
    admin_obj = db.query(admin_model.Admin).filter_by(email=data.email).first()

    if not admin_obj or not verify_password(data.password, admin_obj.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": admin_obj.email})
    return {"access_token": token, "token_type": "bearer"}
