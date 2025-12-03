from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool

p1 = Product(id=1,name= "Mouse", price= 250.23,in_stock=True)
p2 = Product(id=2,name="Monitor",price=245.23)