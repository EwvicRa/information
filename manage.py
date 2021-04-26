from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
# 扩展库里面的session  可以用来指定session保存的位置，点击扩展源码可查看
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

class Config(object):
    """项目的配置"""
    DEBUG = True

    # 设置48字符的随机密匙
    SECRET_KEY = "SECRET_KEY = Ke0McAKwJlAy+/7tgL2pY7pqRZfT3gEfo27JXZMXQ0M8frNLgba3djNBx4O3xiVW"
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置Redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session保存设置  指定 session 保存到 redis 中
    SESSION_TYPE = "redis"
    # 开启session签名  让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGER = True
    # 指定Session 保存的redis，不指定他会帮你指定，这样redis就不能设置端口，地址了
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = True
    # 设置过期时间 源代码中默认是31 天
    PERMANENT_SESSION_LIFETIME = 86400 * 2

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
    return "......333333322222"


if __name__ == '__main__':
    manager.run()
