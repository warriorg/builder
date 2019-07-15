from flask import render_template

from .base import view_bp, dbContext
from code.ssm import SSM


@view_bp.route("/column/table/<table_name>")
def columns(table_name):
    columns = dbContext.columns(table_name)
    table = dbContext.table(table_name)
    if (table and columns):
        ssm = SSM(table, columns, "com.warriorg.test")
        ssm.generate()
    
    return render_template("column.html", columns=columns)
