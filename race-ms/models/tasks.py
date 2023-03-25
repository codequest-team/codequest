from pydantic import BaseModel


class Task(BaseModel):
    level: int
    title: str
    theory_text: str
    task_description: str
    text: str
    expected_result: str



class TaskResponse(BaseModel):
    is_true: bool
    result: str