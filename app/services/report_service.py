import json
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.submission import FormResponse

def get_all_responses(db: Session, form_id: int):
    return db.query(FormResponse)\
        .filter(FormResponse.form_id==form_id)\
        .all()

def get_avg_rating(db: Session, form_id: int):
    rows = get_all_responses(db, form_id)
    ratings = [int(json.loads(r.answers).get("Rating",0)) for r in rows]
    return sum(ratings)/len(ratings) if ratings else 0

def get_avg_by_days(db: Session, form_id: int, days: int):
    since = datetime.utcnow() - timedelta(days=days)

    rows = db.query(FormResponse)\
        .filter(FormResponse.form_id==form_id)\
        .filter(FormResponse.created_at>=since)\
        .all()

    ratings = [int(json.loads(r.answers).get("Rating",0)) for r in rows]
    return sum(ratings)/len(ratings) if ratings else 0
def total_responses(db, form_id):
    return db.query(FormResponse)\
             .filter(FormResponse.form_id==form_id)\
             .count()