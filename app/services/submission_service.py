from sqlalchemy.orm import Session
from app.models.submission import Submission
import json
from app.models.submission import FormResponse
def create_submission(db: Session, form_id: int, name: str, rating: int, answers: str):
    sub = Submission(
        form_id=form_id,
        user_name=name,
        rating=rating,
        answers=answers
    )
    db.add(sub)
    db.commit()
    return sub

def save_response(db: Session, form_id: int, answers: dict):
    response = FormResponse(
        form_id=form_id,
        answers=json.dumps(answers)
    )
    db.add(response)
    db.commit()
    db.refresh(response)
    return response