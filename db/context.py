from db.database import Database
from db.oracle import DbOracle


class Context:
    def __init__(self, dbType, url, user, password):
        if (dbType == 'oracle'):
            self.db = DbOracle(url, user, password)
        if (dbType == 'mysql'):
            return None
        return None

    def userTables(self):
        return self.db.userTables()

    def table(self, table_name):
        return self.db.getTableByName(table_name)

    def columns(self, table_name):
        columns = self.db.columns(table_name)
        return columns
