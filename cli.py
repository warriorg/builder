#!/usr/bin/python3

import sys

from db.context import Context
from code.ssmp import SSMP

dbContext = Context('oracle', 'jdbc:oracle:thin:@192.168.10.128:1521:orcl', 'ENTRY_CENTER_DATA', 'dcjet')

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) == 0): 
        print("python cli.py TABLE_NAME")
        exit(0)

    table_name = args[0].upper()
    
    table = dbContext.table(table_name)
    columns = dbContext.columns(table_name)
    
    ssm = SSMP(table, columns, "com.warriorg.test")
    ssm.generate()
