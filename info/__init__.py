from logging.handlers import RotatingFileHandler
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from sqlalchemy.orm import Session
from config import config


# 初始化数据库
# 在Flask很多扩展里面都可以先初始化扩展对象，然后在调用 init_app 方法去初始化
# 点进去SQLAchemy里面可以看到如果不传值，默认app=NOne，不为空才调用init_app

db = SQLAlchemy()
redis_store = None  # type:StrictRedis

def create_log(config_name):
    # 设置日志的记录等级,
    # level = manage(开发模式)->init->config->调试模式
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):  # 接收传递进来要选择的开发环境
    # 启动 log 日志,
    create_log(config_name)
    # 创建 Flask 环境
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])
    # 通过 app 初始化
    db.init_app(app)
    # 初始化 Redis 存储对象
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启 CSRF 保护 , 只做服务器保护功能 还得自己写 cookie
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    # 注册蓝图 ,注册蓝图是到app里面取，找到flask创建的对象这
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app  # 将flask对象返回去



