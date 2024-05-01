from src.config.database import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(length=16))
    last_name = Column(String(length=16))
    email = Column(String(length=64))
    password = Column(String(length=128))