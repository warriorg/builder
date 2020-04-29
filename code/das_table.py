
from .metadata import ClassMeta, Field



class DasTable():
    def __init__(self, table, columns):
        if table == None:
            raise RuntimeError('表不能为空')
        self.table = table 
        self.columns = columns
        self.convertField()

    def get_class_metadata(self):
        meta = ClassMeta(self.table['name'], self.getTableComment())

        fields = []
        for column in self.columns:
            field = Field(column['name'], column['comment'], column['type'], column['length'],
                          column['precision'], column['scale'], column['primary'], column['nullable'])
            fields.append(field)

        
        meta.fields = sorted(fields, key=lambda k: (-k.primary, k.name.lower()))
        return meta

    def getTableName(self):
        return self.table['name']

    def getTableComment(self):
        return self.table['comment']


    def getPrimaryColumn(self):
        result = [column for column in self.columns if column['primary']]
        return result

    def getColumn(self):
        result = [column for column in self.columns if column['primary'] == False]
        return result

    def convertField(self):
        pass
