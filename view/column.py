from flask import render_template

from .base import view_bp, dbContext


@view_bp.route("/column/table/<table_name>")
def columns(table_name):
    columns = dbContext.columns(table_name)
    return render_template("column.html", columns=columns)
