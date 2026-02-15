from fastapi import FastAPI
from app.database import Base, engine
from app.routes import admin_route ,forms, submissions
from app.routes import forms, submissions
from app.routes import reports
from app.routes import uploads

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(uploads.router)
app.include_router(admin_route.router)
app.include_router(forms.router)
app.include_router(submissions.router)
app.include_router(forms.router)
app.include_router(submissions.router)
app.include_router(reports.router)
@app.get("/")
def root():
    return {"status": "CSAT API Running"}
