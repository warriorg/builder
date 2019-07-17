import jaydebeapi, jpype

from .database import Database

class DbOracle(Database):

    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    def get_jdbc_connection(self):
        driver = 'oracle.jdbc.OracleDriver'
        jarFile = '/Users/warriorg/Code/python/builder/jar/ojdbc6-11.2.0.1.0.jar'
        if jpype.isJVMStarted() and not jpype.isThreadAttachedToJVM():
            jpype.attachThreadToJVM()
            jpype.java.lang.Thread.currentThread().setContextClassLoader(jpype.java.lang.ClassLoader.getSystemClassLoader())
        print(self.url)
        connection = jaydebeapi.connect(driver, self.url, {'user': self.user, 'password': self.password, 'tmode': 'TERA', 'charset': 'UTF8'}, jarFile,)
        return connection

    def userTables(self):
        data = self.execute("""SELECT A.TABLE_NAME, B.COMMENTS FROM USER_TABLES A 
            LEFT JOIN USER_TAB_COMMENTS B ON A.TABLE_NAME=B.TABLE_NAME""")
        result = []
        for table in data:
            result.append({'name': table[0], 'comment': table[1]})
        return result

    def table(self, table_name):
        data = self.execute("""SELECT A.TABLE_NAME, B.COMMENTS FROM USER_TABLES A 
            LEFT JOIN USER_TAB_COMMENTS B ON A.TABLE_NAME=B.TABLE_NAME 
            WHERE  A.TABLE_NAME='%s'""" % table_name)
        if (len(data) > 0):
            return {'name': data[0][0], 'comment': data[0][1]}
        return None

    def columns(self, table_name):
        data = self.execute("""SELECT A.COLUMN_NAME, A.DATA_TYPE, A.DATA_LENGTH, A.DATA_PRECISION, A.DATA_SCALE, A.NULLABLE, B.COMMENTS 
            FROM USER_TAB_COLUMNS A LEFT JOIN USER_COL_COMMENTS B 
            ON A.TABLE_NAME=B.TABLE_NAME AND A.COLUMN_NAME=B.COLUMN_NAME 
            WHERE A.TABLE_NAME='%s' ORDER BY COLUMN_ID ASC""" % table_name)
        result = []
        primary_key = self.table_primary(table_name)
        for column in data:
            result.append({'name': column[0], 'type': column[1], 'primary': column[0] in primary_key,
            'length': column[2], 'precision': column[3], 'scale': column[4], 'nullable':column[5], 'comment': column[6]})
        return result

    def table_primary(self, table_name):
        sql = """SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols
                    WHERE cols.table_name = '%s' AND cons.constraint_type = 'P'
                    AND cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner
                    ORDER BY cols.table_name""" % table_name
        data = self.execute(sql)
        result = []
        for d in data:
            result.append(d[0])
        return result


    def execute(self, sql):
        conn = self.get_jdbc_connection()
        curs = conn.cursor()
        curs.execute(sql)
        result = curs.fetchall()
        curs.close()
        conn.close()
        return result

    def close(self):
        pass
