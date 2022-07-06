import mysql.connector
import config

def connexion():
    con= mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE,
        auth_plugin='mysql_native_password'
    )
    return con

def last_date(id_source):
    con=connexion()
    cur=con.cursor()
    cur.execute("SELECT max(date) FROM data where id_source = %s",(id_source,))
    res = cur.fetchone()
    if res[0]!=None:
        return(res[0])
    else:
        return config.DATE_MIN

con=connexion()
cur=con.cursor()
cur.execute("SELECT * FROM source")
res = cur.fetchall()
print(res)