from pydantic import BaseModel,Field
from typing import Optional

class Employee(BaseModel):
    id : int
    name = str = Field(
        ...,
        min_length=3,
        max_length=15,
        description="Employee Name",
        examples= "Tejas Mankar"   
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        ge = 10000,
        description="Anual Salary"
    )
class User(BaseModel):
    email : str = Field(
        ...,
        regex = r''
    )
    phone : str = Field(
        ...,
        regex=r''
    )
    age = int = Field(
        ...,
        ge=0,
        le=100,
        description="Age in Years",
    )
    discount : float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage"
    )

    