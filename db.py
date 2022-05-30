import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', "sqlite:///data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('DB_TRACK_MODIFICATIONS', False)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = declarative_base()