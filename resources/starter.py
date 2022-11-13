import pymysql
import pandas as pd

class Db_Initializer:
    def __init__(self):
        self.tables = [
            'User', 'Schedule', 'Group'
        ]
        self.fields = {
            'User': [('user_id', 'varchar(25)'), ('user_name','varchar(25)'),
                    ('first_name', 'varchar(25)'), ('last_name', 'varchar(25)'), ('email', 'varchar(25)'),
                    ('group_id', 'varchar(25)')],
            'Schedule': [('schedule_id', 'varchar(25)'), ('schedule_name', 'varchar(25)'), 
                        ('start_time', 'DATETIME'), ('end_time', 'DATETIME'), ('type', 'varchar(25)'),
                        ('user_id', 'varchar(25)')],
            'Group': [('group_id', 'varchar(25)'), ('group_name', 'varchar(25)')],
        }

        self.pkeys = {
            'User': ['user_id'],
            'Schedule': ['schedule_id'],
            'Group': ['group_id'],
        }

        self.fkeys =  {
            'User': [('group_id', 'WeMeet.Group(group_id)')],
            'Schedule': [('user_id', 'WeMeet.User(user_id)')],
            'Group': [],
        }

        self.table_creation_order = ['Group', 'User', 'Schedule']

        self.inputs = {
            "Group" : [
            "1,Team1",
            "2,Team2"
        ],
            "User": [
            "1,jackieryu,Jackie,Ryu,br2543@columbia.edu,1",
            "2,danielkim,Daniel,Kim,sk4539@columbia.edu,1",
            "3,harrylee,Harry,Lee,jl5271@columbia.edu,1",
            "4,jainryu,Jain,Ryu,jr3990@columbia.edu,2",
            "5,jamesjo,James,Jo,sj3014@columbia.edu,2"
        ], "Schedule" : [
            "1,cloud_computing,1000-01-01 00:00:00,9999-12-31 23:59:59,schedule,1",
            "2,ai,1000-01-01 00:00:00,9999-12-31 23:59:59,schedule,2",
            "3,idk,1000-01-01 00:00:00,9999-12-31 23:59:59,schedule,3",
            "4,busy,1000-01-01 00:00:00,9999-12-31 23:59:59,schedule,4",
            "5,soju,1000-01-01 00:00:00,9999-12-31 23:59:59,schedule,5"
        ]}

    def _get_connection(self):
        """
        # DFF TODO There are so many anti-patterns here I do not know where to begin.
        :return:
        """

        # DFF TODO OMG. Did this idiot really put password information in source code?
        # Sure. Let's just commit this to GitHub and expose security vulnerabilities
        #
        conn = pymysql.connect(
            host="wemeet.cmp9jrts2y89.us-east-1.rds.amazonaws.com",
            port=3306,
            user="dbuser",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    def init_schema(self):
        sql = "create database if not exists {0};"
        mysql = sql.format("WeMeet")
        conn = self._get_connection()
        with conn.cursor() as cursor:
            res = cursor.execute(mysql)

    def fetch_schemas(self):
        sql = "show databases;"
        conn = self._get_connection()        
        with conn.cursor() as cursor:
            res = cursor.execute(sql)
            return cursor.fetchall()

    def init_tables(self):
        sql = "create table if not exists WeMeet.{0} ("
        conn = self._get_connection()
        for table in self.table_creation_order:
            mysql = sql.format(table)
            field_details = self.fields[table]
            for field_detail in field_details:
                mysql = mysql + f" {field_detail[0]} {field_detail[1]},"
            for pkey in self.pkeys[table]:
                mysql = mysql + f" primary key ({pkey}),"
            for fkey in self.fkeys[table]:
                mysql = mysql + f" foreign key ({fkey[0]}) references {fkey[1]},"
            mysql = mysql[:-1] + ");"
            print(mysql)
            with conn.cursor() as cursor:
                #cursor.execute('use WeMeet;')
                res = cursor.execute(mysql)
    
    def fetch_tables(self):
        sql = "show tables;"
        conn = self._get_connection()
        with conn.cursor() as cursor:
            cursor.execute("use WeMeet;")
            res = cursor.execute(sql)
            return cursor.fetchall()

    def insert_input(self):
        conn = self._get_connection()
        with conn.cursor() as cursor:
            for table, input in self.inputs.items():
                cursor.execute("use WeMeet;")
                fields = [table[0] for table in self.fields[table]]
                fields = ",".join(fields)
                mysql = f"insert into WeMeet.{table} ({fields}) values "
                for row in input:
                    row = row.split(",")
                    row = [f"'{item}'" for item in row]
                    row = ",".join(row)
                    mysql = mysql + "(" + row + "),"
                mysql = mysql[:-1]
                print(mysql)
                cursor.execute(mysql)

            return cursor.fetchall()



if __name__ == "__main__":
    starter = Db_Initializer()
    starter.init_schema()
    starter.fetch_schemas()
    starter.init_tables()
    starter.insert_input()

