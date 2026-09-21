from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints

class UserCreate(BaseModel):
    user_id: int = Field(gt=0)
    name: Annotated[str, StringConstraints(min_lenght=2, max_lenght=50)]
    email: EmailStr
    age: int = Field(gt=18, lt=120)
    student_id: Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]


