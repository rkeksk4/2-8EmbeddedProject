import sys
import MySQLdb as mysql

try:
    con = mysql.connect('localhost', 'root', 'mysql!pi1', 'db_no_sleep')

    cur = con.cursor()
    sql = "SELECT 1 FROM DUAL;"
    cur.execute(sql)

    for i in range(cur.rowcount):
        row = cur.fetchone()
        print row[0]

except mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
