from flask import Blueprint

"""
创建蓝图三步骤
1 导入
2 创建对象
3 放进去
"""

index_blu = Blueprint("index", __name__,template_folder="templates",
                      # url_prefix="/index",
                      static_folder="static")

# 当前文件夹里面没有主页参数，需要导进来才可以访问到
from .views import index1



