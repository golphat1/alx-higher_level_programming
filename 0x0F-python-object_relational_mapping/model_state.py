#!/usr/bin/python3
"""
class definition of stste and instance Base = declarative_base()
State class: inherites from Base
Links to the MYSQL table states
Class attribute id represents a column of an auto-generated
unique integer, can't be null
class attribute name that represents a column of a string
Use SQLAlchemy
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a Base instance
Base = declarative_base()


# Define the State class
class State(Base):
    """
    Represents a state in the hbtn_0e_4_usa database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
