# __init__.py  初始化文件，创建flask应用

from flask import Flask
from .views import blue

# 创建flask应用，并且返回app
def create_app():
    app=Flask(__name__)
    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    return app