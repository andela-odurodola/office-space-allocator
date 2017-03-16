#!/usr/local/bin/python3

from sqlalchemy import Column, create_engine, Integer, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DatabaseManager(object):
    """Data persistence."""

    def __init__(self, db_name):
        """Constructor function for the class."""
        self.db_name = db_name
        self.engine = create_engine('sqlite:///' + self.db_name, echo=False)
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)


class OfficeRooms(Base):
    """Mapped Office class with it's table."""

    __tablename__ = 'office_room'

    room_id = Column(Integer, primary_key=True)
    room_info = Column(PickleType)


class LivingRooms(Base):
    """Mapped Livingspace class with it's table."""

    __tablename__ = 'living_space'

    livingspace_id = Column(Integer, primary_key=True)
    livingspace_info = Column(PickleType)


class Persons(Base):
    """Mapped Person dictionary with it's table."""

    __tablename__ = 'person'

    persons_id = Column(Integer, primary_key=True)
    person_info = Column(PickleType)
