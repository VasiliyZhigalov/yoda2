from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///C:\Projects\Business\yoda2\yodadatabase.db", echo=True)
session_maker = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_session():
    with sessionmaker() as session:
        return session
