from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.submission import SubmissionCreate
from app.services.submission_service import create_submission
from app.schemas.submission import SubmitForm
from app.services.submission_service import save_response
from app.schemas.form import FormOut
from app.models.form import Form
router = APIRouter(prefix="/submit", tags=["Submissions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{form_id}")
def submit(form_id: int, data: SubmissionCreate, db: Session = Depends(get_db)):
    return create_submission(
        db,
        form_id,
        data.user_name,
        data.rating,
        data.answers
    )


@router.post("/public/{slug}")
def submit_public(slug:str,
                  data:SubmitForm,
                  db:Session=Depends(get_db)):

    form = db.query(Form).filter(Form.slug==slug).first()
    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form not found with this slug"
        )

    return save_response(db, form.id, data.answers)
