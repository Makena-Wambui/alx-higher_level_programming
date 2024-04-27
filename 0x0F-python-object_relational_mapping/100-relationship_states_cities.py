#!/usr/bin/python3

"""
Write a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from model_state import Base, State
from model_city import City
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

    # create a state
    calif = State(name="California")

    # create a city
    sf = City(name="San Francisco")

    # add that new city to the list of cities
    calif.cities.append(sf)

    session.add_all([calif, sf])

    # commit the transaction
    session.commit()
