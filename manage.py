from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
# 扩展库里面的session  可以用来指定session保存的位置，点击扩展源码可查看
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import *


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

# 初始化Redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF保护 , 只做服务器保护功能 还得自己写cookie
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

# 使用flask—script的命令格式操作flask，先连接一下
manager = Manager(app)
# 将app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route("/")
def index1():
    session["name"] = "ykl"
    return "Welcome my house"


if __name__ == '__main__':
    manager.run()
