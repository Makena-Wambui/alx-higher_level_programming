#!/usr/bin/python3

"""
Write a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create a connection to our database using create_engine()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    The delete() function generates a new instance of Delete
    which represents a DELETE statement in SQL,
    that will delete rows from a table.
    """

    # create a delete statement
    stmt = delete(State).where(State.name.like('%a%'))

    # execute the delete statement
    session.execute(stmt)

    session.commit()
