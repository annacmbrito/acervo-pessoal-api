from typing import Any, Type
from sqlalchemy.orm import Session
from src.routes.commons.schemas import OrderDirection, Page
from src.config.database import Base

class BaseService:
    def __init__(self, session: Session, type: Type[Base]):
        self.session = session
        self.type = type

    def save(self, model: Any):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model
    
    def exists(self, condition: Any): 
        return self.filter(condition).first() is not None
    
    def filter(self, condition: Any): 
        return self.session.query(self.type).filter(condition)
    
    def find_all(self, page: Page, filter: Any | None = None):
        result = self.session.query(self.type)
        if filter is not None:
            result = result.filter(*filter)
        page.number_of_elements = result.count()
        if page.sort_by is not None:
            order_column = getattr(self.type, page.sort_by)
            query_order = order_column.asc() if page.order == OrderDirection.ASC else order_column.desc()
            result = result.order_by(query_order)
        if page.size is not None and page.size >= 0:
            result = result.limit(page.size).offset(page.size * page.offset)
        page.content = result.all()
        return page.model_dump()
    
    def delete_by_id(self, id: int):
        record = self.filter(self.type.id == id).first()
        self.session.delete(record)
        self.session.commit()