import os
from sqlmodel import create_engine, Session
from sqlmodel import SQLModel

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/app.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)

from contextlib import contextmanager

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session
