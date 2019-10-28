from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)
    user_type = Column(String)

    items = relationship('Item', backref='User',
        cascade='all, delete-orphan', lazy='dynamic')

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    width = Column(Float)
    height = Column(Float)
    length = Column(Float)
    weight = Column(Float)

    # Defining One to Many relationships with the relationship function on the Parent Table
    items = relationship('Item', backref='Product',
        cascade='all, delete-orphan', lazy='dynamic')

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)

    # Defining the Foreign Key on the Child Table
    product_id = Column(Integer, ForeignKey('products.id'))
    product = Column(String)

    seller_id = Column(Integer, ForeignKey('users.id'))
    seller = Column(String)

    price = Column(Float)
    quantity = Column(Boolean)

# create tables
Base.metadata.create_all(engine)
