#!/usr/bin/python3

"""
Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
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

    """
    use the filter or filter_by methods in conjunction with
    the like operator to find all records in a table
    that contain a specific substring, such as the letter 'a'.
    The like operator allows you to specify a pattern to
    match against the values in a column.
    """
    # Call .all() on the query to retrieve all records that match the query
    records_with_a = session.query(State).filter(State.name.like('%a%')).all()
    # print(type(records_with_a))
    for record in records_with_a:
        print("{}: {}".format(record.id, record.name))
