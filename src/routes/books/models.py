from src.config.database import Base
from sqlalchemy import Column, String, Integer

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=32))