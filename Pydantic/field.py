from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id : int
    item : List[str]
    quantities : Dict[str,int]

class BlogPost(BaseModel):
    title : str
    context : str
    image_url : Optional[str] = None
    
cart_data = {
    "user_id" : 123,
    "item" : ["Laptop","mouse","Keyboard"],
    "quantities" : {"laptop" : 1, "mouse" : 2, "keyborad" : 3}, 
}

cart = Cart(**cart_data)