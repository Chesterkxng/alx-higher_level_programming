#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]
    input = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=usr,
                         passwd=pwd, db=dtb, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (input,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
