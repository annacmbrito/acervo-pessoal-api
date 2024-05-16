from src.config.database import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=128))
    description = Column(String)
    comment = Column(String)
    pages = Column(Integer)
    rating = Column(Integer)
    status = Column(String(length=32))
    author_id = Column(Integer, ForeignKey('author.id'))
    language_id = Column(Integer, ForeignKey('language.id'))
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    subcategory_id = Column(Integer, ForeignKey('subcategory.id'))

    author = relationship("Author", back_populates="books", lazy=False)
    language = relationship("Language", back_populates="books", lazy=False)
    publisher = relationship("Publisher", back_populates="books", lazy=False)
    category = relationship("Category", back_populates="books", lazy=False)
    subcategory = relationship("Subcategory", back_populates="books", lazy=False)