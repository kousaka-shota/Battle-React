from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False},#echo=True
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

async def get_db():
    with SessionLocal() as session:
        yield session

Base = declarative_base()