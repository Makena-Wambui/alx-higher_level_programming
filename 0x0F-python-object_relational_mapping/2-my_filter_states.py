#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
    # You must use format to create the SQL query with the user input
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'".format(sys.argv[4]))

    rows = cur.fetchall()
    for all in rows:
        print(all)
    cur.close()
    mydb.close()
