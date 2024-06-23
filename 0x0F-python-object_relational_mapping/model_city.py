#!/usr/bin/python3

"""
This file contains the definition of a class City.
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Class: City

    A subclass of Base.

    Attributes: id, name, states_id

    Linked to the table cities
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    states = relationship('State', back_populates="cities")
