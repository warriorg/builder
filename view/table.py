from flask import render_template

from .base import view_bp, dbContext


@view_bp.route("/")
def tables():
    tables = dbContext.userTables()
    return render_template("index.html", tables=tables)
