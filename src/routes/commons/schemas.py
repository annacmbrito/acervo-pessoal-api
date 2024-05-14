from pydantic import BaseModel, Field
from typing import List, Any
from enum import Enum

class OrderDirection(Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class Page(BaseModel):
    size:int | None = None
    offset:int = Field(0, ge=0)
    order_by:str = 'id'
    order_direction: OrderDirection = OrderDirection.ASC
    number_of_elements: int = 0
    content:List[Any] = []