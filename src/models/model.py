from sqlalchemy import Column, Integer, Text, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, unique=True)
    name = Column(Text)
    role = Column(Text)
    latitude = Column(Text)
    longitude = Column(Text)


class UserQuery(Base):
    __tablename__ = 'user_queries'

    id = Column(Integer, primary_key=True, unique=True)
    product = Column(Text)
    quantity = Column(Numeric)
    unit = Column(Text)
    filter = Column(Text)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE'))


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(Text)
    price = Column(Numeric)
    image = Column(Text)
    href = Column(Text)
    description = Column(Text)
    market_id = Column(Integer, ForeignKey('markets.id'))
    user_query_id = Column(Integer, ForeignKey('user_queries.id'))


class Market(Base):
    __tablename__ = 'markets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    number = Column(Text)
    href = Column(Text)
