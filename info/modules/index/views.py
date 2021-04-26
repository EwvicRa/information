from . import index_blu
from flask import session


@index_blu.route("/")
def index1():
    session["name"] = "小米"

    return "Welcome my house"
