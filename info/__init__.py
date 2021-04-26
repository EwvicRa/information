from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy.orm import Session
from config import *

# 初始化数据库
# 在Flask很多扩展里面都可以先初始化扩展对象，然后在调用 init_app 方法去初始化
# 点进去SQLAchemy里面可以看到如果不传值，默认app=NOne，不为空才调用init_app
db = SQLAlchemy()


def create_app(config_name):  # 接收传递进来要选择的开发环境
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])
    # 通过app初始化
    db.init_app(app)
    # 初始化Redis 存储对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启CSRF保护 , 只做服务器保护功能 还得自己写cookie
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    return app  # 将flask对象返回去
