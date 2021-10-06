import pymysql

db = pymysql.connect(
    host = '127.0.0.1',
    user= 'root',
    passwd='1234',
    db='kang_nodjs_db',
    charset= 'utf8'
)

cur =db.cursor()
cur.execute("Select * FROM USERS")

rows = cur.fetchall()
print(rows)
db.close()