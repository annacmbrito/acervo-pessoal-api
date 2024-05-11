from src.config.database import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

class Subcategory(Base):
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=32))
    category_id = Column(Integer, ForeignKey('category.id'))

    books = relationship("Book", back_populates="subcategory")
    category = relationship("Category", back_populates="subcategories")