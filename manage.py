from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db
import logging

# 通过指定配置名字创建对应的配置app，接收返回来的flask的app对象
# create_app 就类似于工厂方法，传不同参数，制造不同的小黄车
app = create_app("deverlopmentconfig")
# 使用flask—script的命令格式操作flask，先连接一下
manager = Manager(app)
# 将app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route("/")
def index1():
    session["name"] = "ykl"

    # 测试打印日志
    # logging.debug("测试debug1")
    # logging.error("测试error3")
    # current_app.logger.error("error")
    return "Welcome my house"


if __name__ == '__main__':
    manager.run()
