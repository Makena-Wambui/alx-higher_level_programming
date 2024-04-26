#!/usr/bin/python3

"""i
Write a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.

Your script should take 4 arguments: mysql username,
mysql password, database name and state name
to search (SQL injection free).
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

    To be SQL Injection free, avoid directly interplolating
    user input into sql queries.
    Use parametized queries
    """

    user_input = sys.argv[4]
    matched = session.query(State).filter(State.name.
                                          like(user_input)).all()
    if matched:
        matched = matched[0]
        print(matched.id)
    else:
        print("Not found")
