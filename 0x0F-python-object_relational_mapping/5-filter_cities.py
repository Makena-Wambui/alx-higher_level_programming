#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

Should be SQL Injection free.
"""

import MySQLdb

# sys.argv for the arguments passed to the script when executing it.
import sys

if __name__ == "__main__":
    # create a connection to the database
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # create a cursor object
    cur = mydb.cursor()

    # use the execute  function
    state_name = sys.argv[4]
    cur.execute("SELECT cities.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id=states.id "
                "WHERE states.name=%s", (state_name, ))

    rows = cur.fetchall()

    # fetchall returns a list of tuples.
    # use list comprehension to extract the city names fom this list.
    cities_names = [item[0] for item in rows]
    print(", ".join(cities_names))
    cur.close()
    mydb.close()
