from pydantic import BaseModel
from typing import List, Any

class Page(BaseModel):
    size:int
    offset:int
    sort_by:str
    order: str
    number_of_elements: int = 0
    content:List[Any] = []