#!/usr/bin/python3
import MySQLdb

# Every DB-API statement that you execute has the potential to raise an exception.
# Any time you execute a database query you should surround it with a try/exception block. This includes connections, cursor requests, and statement executions.
# use MySQLdb.Error to catch all db exceptions

db = MySQLdb.connect(host="localhost", user="root", passwd="Lucibel96", db="JAKE")
cur = db.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS Song  (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")

songs = ('Suzanna', 'Extravaganza', 'Rhumba Japani')
for song in songs:
    cur.execute("INSERT INTO Song (title) VALUES (%s)", (song,))
    print("id: {}".format(cur.lastrowid))

try:
    cur.execute("SELECT * FROM Song")
    # TO fetch all at once
    rows = cur.fetchall()
except MySQLdb.error, e:
    try:
        print("MySQL error {}: {}".format(e.args[0], e.args[1]))
    except IndexError:
        print("MySQL Error: {}".format(str(e)))
for row in rows:
    for column in row:
        print("{}".format(column))
    print()

# To fetch one at a time
cur.execute("SELECT * FROM Song WHERE id = 10")
myentry = cur.fetchone()
print("id= {}, title={}".format(myentry[0], myentry[1]))

# clean up
# close all open cursors
# close all open db connections
# each cursor and each db connection has a close function.
# call close for each instance you created.
cur.close()
db.close()

