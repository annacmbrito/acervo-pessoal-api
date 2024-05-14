from src.config.database import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=32))
    description = Column(String)
    comment = Column(String)
    rating = Column(Integer)
    available = Column(Boolean)
    author_id = Column(Integer, ForeignKey('author.id'))
    language_id = Column(Integer, ForeignKey('language.id'))
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    subcategory_id = Column(Integer, ForeignKey('subcategory.id'))

    author = relationship("Author", back_populates="books")
    language = relationship("Language", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")
    category = relationship("Category", back_populates="books")
    subcategory = relationship("Subcategory", back_populates="books")