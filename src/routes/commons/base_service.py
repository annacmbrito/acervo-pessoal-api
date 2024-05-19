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
        result = self.__apply_filters(result, filter)
        page.number_of_elements = result.count()
        result = self.__apply_ordering(result, page)
        result = self.__apply_pagination(result, page)
        page.content = result.all()
        return page.model_dump()
    
    def __apply_joins(self, query, joins):
        if joins:
            for table in joins:
                query = query.join(table)
        return query

    def __apply_filters(self, query, filters):
        if filters:
            query = query.filter(*filters)
        return query
    
    def __apply_ordering(self, query, page):
        if page.order_by:
            order_column = self.__get_order_column(page.order_by)
            query_order = order_column.asc() if page.order_direction == OrderDirection.ASC else order_column.desc()
            query = query.order_by(query_order)
        return query

    def __get_order_column(self, order_by):
        if '.' in order_by:
            relations = order_by.split('.')
            column_name = relations.pop()
            current_model = self.type
            for relation in relations:
                current_model = getattr(current_model, relation).property.mapper.class_
            return getattr(current_model, column_name)
        else:
            return getattr(self.type, order_by)

    def __apply_pagination(self, query, page):
        if page.size and page.size >= 0:
            query = query.limit(page.size).offset(page.size * page.offset)
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