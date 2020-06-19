#!/usr/bin/env python

import sys

from db.context import Context
from code.ssm import SSM

dbContext = Context('oracle', 'jdbc:oracle:thin:@192.168.10.133:1521:JGDBM', 'GWSTD', 'chinaport2018')

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 2): 
        print("python cli.py TABLE_NAME module [package]")
        exit(0)

    table_name = args[0].upper()
    
    table = dbContext.table(table_name)
    if table == None:
        print("数据库里面有这张表吗？")
        exit(0)

    columns = dbContext.columns(table_name)

    module = args[1].lower()
    package = "com.dcjet.cs"
    if (len(args) > 2):
       package = args[2]
    
    ssm = SSM(table, columns, module, package) 
    ssm.generate()
