from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.config import settings

# SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123qwe@localhost:5432/dz11"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()