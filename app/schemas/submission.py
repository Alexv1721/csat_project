from pydantic import BaseModel
from typing import Dict

class SubmissionCreate(BaseModel):
    user_name: str
    rating: int
    answers: str


class SubmitForm(BaseModel):
    answers: Dict
