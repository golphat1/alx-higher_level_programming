#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


# Define the City class
class City(Base):
    """
    Represents a city in the hbtn_0e_14_usa database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
