from pydantic import BaseModel
from typing import List, Any

class Page(BaseModel):
    size:int
    offset:int
    number_of_elements: int = 0
    content:List[Any] = []