import json
from sqlalchemy.orm import Session
from app.models.form import Form
import uuid
def create_form(db, title, description, questions, admin_id):
    slug = str(uuid.uuid4())[:8]

    form = Form(
        title=title,
        description=description,
        questions=json.dumps(questions),
        slug=slug,
        admin_id=admin_id
    )

    db.add(form)
    db.commit()
    db.refresh(form)
    return form
def get_admin_forms(db: Session, admin_id: int):
    return db.query(Form).filter(Form.admin_id == admin_id).all()

def get_form_by_id(db, form_id):
    return db.query(Form).filter(Form.id == form_id).first()