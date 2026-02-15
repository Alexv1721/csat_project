from pydantic import BaseModel
from typing import List, Optional,Dict

class Question(BaseModel):
    label: str
    type: str              # text, number, radio, checkbox, file, textarea
    options: Optional[list] = None
    required: bool = False

class FormCreate(BaseModel):
    title: str
    description: str
    questions: List[Question]

class FormOut(BaseModel):
    id: int
    title: str
    description: str
    questions: list

    class Config:
        from_attributes = True



class FormCreate(BaseModel):
    title: str
    description: str
    questions: List[Dict]