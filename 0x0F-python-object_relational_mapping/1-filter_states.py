#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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

    # use the execute  function and LIKE BINARY To force case sensitivity
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")

    rows = cur.fetchall()
    for all in rows:
        print(all)
    cur.close()
    mydb.close()
