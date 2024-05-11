from src.config.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=32))

    books = relationship("Book", back_populates="category")
    subcategories = relationship("Subcategory", back_populates="category", cascade="all, delete")