#!/usr/bin/python3

"""
Write a script that prints all City objects
from the database hbtn_0e_14_usa
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

    my_cities = (session.query(State, City)
                 .join(City, State.id == City.state_id)
                 .order_by(City.id).all())
    for state, city in my_cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # commit the transaction
    session.commit()
