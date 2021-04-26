from . import index_blu
from info import redis_store

@index_blu.route("/")
def index1():
    redis_store.set("weight", "187")

    return "Welcome my house"
