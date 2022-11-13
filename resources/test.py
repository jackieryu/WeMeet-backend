import pymysql

conn = pymysql.connect(
            host="wemeet.cmp9jrts2y89.us-east-1.rds.amazonaws.com",
            port=3306,
            user="dbuser",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

sql = "show databases;"
with conn.cursor() as cursor:
    res = cursor.execute(sql)   
    print(res)
    print(cursor.fetchall())