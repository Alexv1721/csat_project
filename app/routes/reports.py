from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
import pandas as pd

import json
from fastapi.responses import FileResponse
from app.core.jwt import get_current_admin
from app.services.report_service import (
    get_avg_rating,
    get_avg_by_days,
    get_all_responses
)

router = APIRouter(prefix="/reports", tags=["Reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{form_id}")
def form_report(form_id:int,
                admin=Depends(get_current_admin),
                db:Session=Depends(get_db)):

    return {
        "overall_avg": get_avg_rating(db, form_id),
        "avg_30_days": get_avg_by_days(db, form_id, 30),
        "avg_60_days": get_avg_by_days(db, form_id, 60),
        "avg_90_days": get_avg_by_days(db, form_id, 90)
    }

@router.get("/{form_id}/responses")
def all_responses(form_id:int,
                  admin=Depends(get_current_admin),
                  db:Session=Depends(get_db)):
    return get_all_responses(db, form_id)


@router.get("/{form_id}/export")
def export_excel(form_id:int,
                 admin=Depends(get_current_admin),
                 db:Session=Depends(get_db)):

    rows = get_all_responses(db, form_id)

    data = []
    for r in rows:
        data.append(json.loads(r.answers))

    df = pd.DataFrame(data)
    file_name = f"form_{form_id}.xlsx"
    df.to_excel(file_name, index=False)

    return FileResponse(file_name)

@router.get("/{form_id}/summary")
def summary(form_id:int,
            admin=Depends(get_current_admin),
            db:Session=Depends(get_db)):

    return {
        "total_responses": total_responses(db, form_id),
        "overall_avg": get_avg_rating(db, form_id),
        "avg_30": get_avg_by_days(db, form_id,30),
        "avg_60": get_avg_by_days(db, form_id,60),
        "avg_90": get_avg_by_days(db, form_id,90)
    }