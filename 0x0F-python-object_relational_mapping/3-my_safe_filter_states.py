#!/usr/bin/python3
"""
    a script takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name
    matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    av = argv
    if len(av) == 5:
        user = argv[1]
        passwd = argv[2]
        db_name = argv[3]

        try:
            db = MySQLdb.connect(
                    host='localhost', port=3306,
                    user=user, passwd=passwd, db=db_name
                )
            cur = db.cursor()
            cur.execute(
                    "SELECT * FROM states WHERE BINARY name = %s \
                    ORDER BY id ASC", (argv[4],))
            for each in cur.fetchall():
                print(each)
            cur.close()
            db.close()
        except MySQL.error:
            print("Connection failed")
    else:
        print("Usage: <py script> <user> <password> <db>")
