from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config import settings

DB_URL = settings.DB_URL
engine = create_engine(DB_URL)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass