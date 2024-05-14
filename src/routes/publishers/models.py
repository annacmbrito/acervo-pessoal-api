from src.config.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=32))

    books = relationship("Book", back_populates="publisher")