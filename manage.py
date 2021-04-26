from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

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
