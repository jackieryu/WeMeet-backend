import pymysql


class Student:

    def __init__(self):
        # You may have to put code here.
        pass

    def get_by_id(self, ID):
        # Connect to DB.
        connect = pymysql.connect(host='localhost', user='dbuser', password='dbuserdbuser', database='db_book')

        # Form SQL
        # Run query
        with connect:
            with connect.cursor() as cursor:
                cursor.execute("SELECT * FROM student WHERE ID=%s",ID)

        # return result
        data = cursor.fetchall()
        return data