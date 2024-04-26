#!/usr/bin/python3

"""
Write a script that prints the first State object
from the database hbtn_0e_6_usa
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

    # create a session, an intermediary btwn your python application and the db
    Session = sessionmaker(bind=engine)

    # create a Session object
    session = Session()

    # query the first object using first()
    # returns the first result of the query, or None if there are no results.
    first_entry = session.query(State).first()
    # If the table states is empty, print Nothing followed by a new line
    if first_entry:
        print("{}: {}".format(first_entry.id, first_entry.name))
    else:
        print("Nothing")
