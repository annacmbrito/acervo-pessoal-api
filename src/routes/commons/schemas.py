from pydantic import BaseModel, Field
from typing import List, Any, Union
from enum import Enum

class OrderDirection(Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class Page(BaseModel):
    size:int | None = None
    offset:int = Field(0, ge=0)
    sort_by:str
    order: OrderDirection
    number_of_elements: int = 0
    content:List[Any] = []