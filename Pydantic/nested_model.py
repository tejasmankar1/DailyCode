from pydantic import BaseModel
from typing import List, Optional



class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address

address = Address(
    street="123 something",
    city="Nagpur",
    postal_code= "10001",
)

user = User(

    id=101,
    name= "Tejas",
    address= address,
)
print(user)