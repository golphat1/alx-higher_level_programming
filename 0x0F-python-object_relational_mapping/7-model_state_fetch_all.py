#!/usr/bin/python3
"""
Script that lists all State objects from database hbtn_0e_6_usa
Takes 3 arguments: mysql username, mysql password and databse name
Use SQLAlchemy
Import State and Base from model_state - from model_state
import Base, State
Result be sorted in ascending order by states.id
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """Database credentials"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create a connection to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    # Bind the engine to the Base instance
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all State objects, sorted by id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
