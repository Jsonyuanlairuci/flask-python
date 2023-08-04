# __init__.py  初始化文件，创建flask应用

from flask import Flask
from .views import blue
from .exts import init_exts

# 创建flask应用，并且返回app
def create_app():
    app=Flask(__name__)
    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置sqllit数据库
    # db_uri='sqlite:///sqlite3.db'
    

    # 配置mysql数据库    mysql用户名：密码@服务器地址：端口/数据库名
    db_uri='mysql+pymysql://root:root@127.0.0.1:3306/flaskdb'
    app.config['SQLALCHEMY_DATABASE_URI']=db_uri      #配置数据库连接
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False    #禁止对象追踪修改（消耗资源）
    
   
    
    # 初始化插件
    init_exts(app=app)
    return app