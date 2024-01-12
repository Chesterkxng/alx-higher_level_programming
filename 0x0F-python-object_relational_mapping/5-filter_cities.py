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
    stmt = "SELECT name FROM cities WHERE cities.state_id = " +\
           "(SELECT id FROM states WHERE name = %s) ORDER BY id ASC"
    cur.execute(stmt, (input,))
    query_rows = cur.fetchall()
    n = len(query_rows)
    for i in range(n):
        print(rows[i][0], end="")
        if (i < n - 1):
            print(", ", end="")
    print("")
    cur.close()
    db.close()
