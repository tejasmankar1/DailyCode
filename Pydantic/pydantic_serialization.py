from pydantic import BaseModel, ConfigDict
from typing import  List,Optional
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool
    createdAt : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders= {
            datetime : lambda v : v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

user = User(
    id=101,
    name="Tejas",
    email="teja@gmail.com",
    createdAt=datetime(2025,12,4,10,45,20),
    address= Address(
        street="Something",
        city="Nagpur",
        zip_code="008948"
    ),
    is_active=False,
    tags=["Premium", 'subscriber']
)


python_dict = user.model_dump()
print(user)
print("="*80)
print(python_dict)

json_str = user.model_dump_json()
print(json_str)