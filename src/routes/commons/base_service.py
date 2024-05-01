from typing import Any, Type
from sqlalchemy.orm import Session
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