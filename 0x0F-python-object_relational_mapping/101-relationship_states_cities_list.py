#!/usr/bin/python3

"""
Write a script that lists all State objects, and
corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import City


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

    try:
        allStates = session.query(State).order_by(State.id).all()
        for state in allStates:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print("    ", end="")
                print("{}: {}".format(city.id, city.name))
    except Exception as e:
        print(e)
    finally:
        session.close()
