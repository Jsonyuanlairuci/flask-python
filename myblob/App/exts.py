# 插件管理
# 1:导入三方插件
from flask_sqlalchemy import SQLAlchemy      #orm
from flask_migrate import Migrate


# 2：初始化
db=SQLAlchemy()      #orm
migrate=Migrate()

# 3：和app对象绑定
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)