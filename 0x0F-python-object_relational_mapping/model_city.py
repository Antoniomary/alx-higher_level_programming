#!/usr/bin/python3
"""
   a python file that contains the class definition of a State
   and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """a class that defines a City"""
    __tablename__ = "cities"

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(
            String(128),
            nullable=False
        )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
        )

    state = relationship('State', backref='cities')
