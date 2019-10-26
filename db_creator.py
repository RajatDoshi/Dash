from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # address_id = Column(Integer, ForeignKey("addresses.id"))
    # address = relationship("Address", backref=backref(
    #     "users", order_by=id))

    def __repr__(self):
        return "{}".format(self.name)

class Album(Base):
    """"""
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    publisher = Column(String)
    media_type = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref(
        "albums", order_by=id))

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)

# create tables
Base.metadata.create_all(engine)
