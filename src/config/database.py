from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url, echo=False)
DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()