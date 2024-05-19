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
    
    def find_all(self, page: Page, filter: Any | None = None, joins: Any | None = None):
        result = self.session.query(self.type)
        result = self.__apply_joins(result, joins)
        if filter is not None:
            result = result.filter(*filter)
        page.number_of_elements = result.count()
        if page.order_by is not None:
            order_column = getattr(self.type, page.order_by)
            query_order = order_column.asc() if page.order_direction == OrderDirection.ASC else order_column.desc()
            result = result.order_by(query_order)
        if page.size is not None and page.size >= 0:
            result = result.limit(page.size).offset(page.size * page.offset)
        page.content = result.all()
        return page.model_dump()
    
    def __apply_joins(self, query, joins):
        if joins:
            for table in joins:
                query = query.join(table)
        return query
    
    def update_by_id(self, id: int, model: Any):
        record = self.filter(self.type.id == id).first()
        if record is None:
            raise ValueError('Record not found')
        else:
            for key, value in vars(model).items():
                if not key.startswith('_') and hasattr(self.type, key):
                    setattr(record, key, value)
            self.session.commit()
    
    def delete_by_id(self, id: int):
        record = self.filter(self.type.id == id).first()
        if record is not None:
            self.session.delete(record)
            self.session.commit()