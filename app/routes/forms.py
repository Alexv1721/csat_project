from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.form import Form
from app.database import SessionLocal
from app.schemas.form import FormCreate
from app.services.form_service import (
    create_form,
    get_admin_forms
)
from app.core.jwt import get_current_admin
from app.models.form import Form   # <-- IMPORTANT

router = APIRouter(
    prefix="/forms",
    tags=["Forms"]
)


# ------------------------
# DB Dependency
# ------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# CREATE FORM (ADMIN)
# ------------------------
@router.post("/create")
def create_form_api(
    data: FormCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    return create_form(
        db=db,
        title=data.title,
        description=data.description,
        questions=data.questions,
        admin_id=admin.id
    )


# ------------------------
# GET ADMIN FORMS
# ------------------------
@router.get("/my")
def my_forms(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    return get_admin_forms(db, admin.id)


# ------------------------
# PUBLIC FORM BY SLUG
# ------------------------
@router.get("/public/{slug}")
def get_form_public(
    slug: str,
    db: Session = Depends(get_db)
):
    form = db.query(Form).filter(Form.slug == slug).first()

    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form not found"
        )

    return form
