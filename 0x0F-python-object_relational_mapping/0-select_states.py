#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':
    av = argv
    if len(av) == 4:
        user = argv[1]
        passwd = argv[2]
        db_name = argv[3]

        try:
            db = MySQLdb.connect(
                    host='localhost', port=3306,
                    user=user, passwd=passwd, db=db_name
                )
            cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            for each in cur.fetchall():
                print(each)
            cur.close()
            db.close()
        except MySQL.error:
            print("Connection failed")
    else:
        print("Usage: <py script> <user> <password> <db>")
