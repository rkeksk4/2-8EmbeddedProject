import sys
import MySQLdb as mysql

con = None
id = None
pw = None
dbname = None

def init(id_in, pw_in, dbname_in):
    global id, pw, dbname
    id = id_in
    pw = pw_in
    dbname = dbname_in

def connect():
    global con, id, pw, dbname
    con = mysql.connect('localhost', id, pw, dbname)

def test():
    global con

    try:
        connect()
        cur = con.cursor()
        sql = "SELECT 1 FROM DUAL"
        cur.execute(sql)

        for i in range(cur.rowcount):
            row = cur.fetchone()

        print "DB connection success."

        con.close()

    except mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

def insert(tablename, val):
    global con
    
    try:
        connect()
        cur = con.cursor()
        sql = "INSERT INTO " + tablename + " VALUE(" + val + ");"
        cur.execute(sql)
        con.commit()
        con.close()

    except mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

def exeSql(sql):
    global con
    try:
        connect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()

    except mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


