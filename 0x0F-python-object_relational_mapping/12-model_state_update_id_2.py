#!/usr/bin/python3

"""
Write a script that changes the name of a State object
from the database hbtn_0e_6_usa

Change the name of the State where id = 2 to New Mexico
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

    # lets query using a filter operator __eq__
    state = session.query(State).filter(State.id == 2).first()

    # change name of the State
    state.name = "New Mexico"

    # commit the transaction
    session.commit()
    # lets create a new State object
