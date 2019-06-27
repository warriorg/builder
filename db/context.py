from db.database import Database
from db.oracle import DbOracle


class Context:
    def __init__(self, dbType, url, user, password):
        if (dbType == 'oracle'):
            self.db = DbOracle()
            self.db.connect(url, user, password)
        if (dbType == 'mysql'):
            return None
        return None

    def userTables(self):
        return self.db.userTables()

    def columns(self, table_name):
        columns = self.db.columns(table_name)
        return columns
