#
# DFF TODO: Accessing database directly from resource is an anti-pattern.
# You did not learn this from me.
#
import pymysql
import json


class User():

    def __init__(self):
        self.db_schema = 'WeMeet'
        self.db_table = 'User'
        self.db_table_full_name = self.db_schema + "." + self.db_table

    def _get_connection(self):
        """
        # DFF TODO There are so many anti-patterns here I do not know where to begin.
        :return:
        """

        # DFF TODO OMG. Did this idiot really put password information in source code?
        # Sure. Let's just commit this to GitHub and expose security vulnerabilities
        #
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="dbuser",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    def get_resource_by_id(self, id):
        """
        # DFF TODO Will the anti-patterns never end?
        :return:
        """

        sql = "select * from " + self.db_table_full_name + " where nconst=%s"
        conn = self._get_connection()
        cursor = conn.cursor()
        res = cursor.execute(sql, (id))

        if res == 1:
            result = cursor.fetchone()
        else:
            result = None

        return result

    def get_by_template(self,
                        path=None,
                        template=None,
                        field_list=None,
                        limit=None,
                        offset=None):
        pass

    def create(self, new_resource):
        pass

    def update_resource_by_id(self, id, new_values):
        pass

    def delete_resource_by_id(self, id):
        pass


if __name__ == "__main__":

    artists_res = User()

    t_h = artists_res.get_resource_by_id('')
    print(json.dumps(t_h, indent=2))

