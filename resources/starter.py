import pymysql

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
                        ('start_time', 'varchar(25)'), ('end_time', 'varchar(25'), ('type', 'varchar(25'),
                        ('user_id', 'varchar(25')],
            'Group': [('group_id', 'varchar(25'), ('group_name', 'varchar(25')],
        }

        self.pkeys = {
            'User': ['user_id'],
            'Schedule': ['schedule_id'],
            'Group': ['group_id'],
        }

        self.fkeys =  {
            'User': ['group_id'],
            'Schedule': ['user_id'],
            'Group': [],
        }

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
        sql = "create table if not exists WeMeet.{0}"
        conn = self._get_connection()
        for table in self.tables:
            mysql = sql.format(table)
            field_details = self.fields[table]
            for field_detail in field_details:
                if field_detail[0] in self.pkeys[table]:
                    mysql = mysql + f" primary key"
                elif field_detail[0] in self.fkeys[table]:
                    mysql = mysql + f" foreign key"
                mysql = mysql + f" {field_detail[0]} {field_detail[1]},"
            mysql = 
            with conn.cursor() as cursor:
                res = cursor.execute(mysql)
    
    def fetch_tables(self):
        sql = "show tables;"
        conn = self._get_connection()
        with conn.cursor() as cursor:
            cursor.execute("use WeMeet;")
            res = cursor.execute(sql)
            return cursor.fetchall()

if __name__ == "__main__":
    print(
        Db_Initializer().init_tables()
    )