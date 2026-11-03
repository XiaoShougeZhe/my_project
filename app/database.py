import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
print("DATABASE_URL =", os.getenv("DATABASE_URL"))
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:4elovek756@localhost:5432/my_project_db")

SQLALCHEMY_DATABASE__URL = "postgresql://postgres:4elovek756@localhost:5432/my_project_db"
engine = create_engine(SQLALCHEMY_DATABASE__URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()