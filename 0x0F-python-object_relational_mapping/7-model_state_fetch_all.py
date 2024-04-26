#!/usr/bin/python3

"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create a connection to our database using create_engine()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # ensure table is created before creating a session.
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)

    # create a Session object
    session = Session()

    # query the db using the query()
    all_objects = session.query(State).order_by(State.id)

    for obj in all_objects:
        print(f"{obj.id}: {obj.name}")
