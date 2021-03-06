import re
from datetime import datetime

from code.code_util import underline_to_camel, underline_to_java_bean

java_dict = {
    'tinyint': 'Integer',
    'smallint': 'Integer',
    'mediumint': 'Integer',
    'int': 'Long',
    'bool': 'Boolean',
    'bit': 'Boolean',
    'float': 'Float',
    'double': 'Double',
    'real': 'Double',
    'decimal': 'BigDecimal',
    'number': 'BigDecimal',
    'datetime': 'Date',
    'date': 'Date',
    'time': 'Date',
    'timestamp': 'Date'
}

jdbc_dict = {
    'VARCHAR2': 'VARCHAR',
    'DATETIME': 'TIMESTAMP',
    'NUMBER': 'NUMERIC'
}

field_filter = [
    'SID',
    'TRADE_CODE',
    'INSERT_TIME',
    'INSERT_USER',
    'INSERT_USER_NAME',
    'UPDATE_TIME',
    'UPDATE_USER',
    'UPDATE_USER_NAME'
]

def get_java_type(type, precision, scale):
    key = type.lower()
    java_type = 'String'
    if key in java_dict:
        java_type = java_dict[key]

    if java_type == 'BigDecimal':
        if not scale or scale == 0:
            java_type = 'Integer'
            if precision > 10:
                java_type = 'Long' 
    return java_type

def get_jdbc_type(type):
    jdbc_type = type
    if type in jdbc_dict:
        jdbc_type = jdbc_dict[type]
    return jdbc_type

class ClassMeta:
    package = ''
    table = ''
    name = ''
    comment = ''
    fields = []

    def __init__(self, table_name, comment):
        self.table = table_name
        self.name = self.get_class_name(table_name)
        self.comment = comment

    def get_class_name(self, table_name):
        tableName = re.sub('^(T_|F_|P_|V_|IDX_|SEQ_)', "", table_name)
        return underline_to_camel(tableName)

    def get_date(self):
        return datetime.today().strftime('%Y-%m-%d')

class Field:
    column = ''
    name = ''
    comment = ''
    jdbc_type = ''
    java_type = ''
    column_type = ''
    length = None
    precision = None
    scale = None
    primary = False
    nullable = False
    strictMode = False

    def __init__(self, column, comment, type, length, precision, scale, primary, nullable, strictMode = False):
        """
        args: 
            strictMode: javaBean遵守严格模式 I_E_MODEL => IEModel 
        """
        if precision:
            self.precision = int(precision)
        if scale:
            self.scale = int(scale) 
        self.strictMode = strictMode
        self.column = column
        self.filter = column in field_filter
        self.name = self.get_bean_name(column) 
        self.comment = comment
        self.column_type = type
        self.java_type = get_java_type(type, self.precision, self.scale)
        self.jdbc_type = get_jdbc_type(type)
        
        self.length = int(length) 
       
        self.primary = primary
        self.nullable = nullable == 'Y'

    def get_bean_name(self, columnName):
        return underline_to_java_bean(columnName, self.strictMode)

    def __str__(self):
       self.__dict__
