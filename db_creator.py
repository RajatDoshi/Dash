from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String)

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

    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", backref=backref(
        "albums", order_by=id))

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

# create tables
Base.metadata.create_all(engine)
