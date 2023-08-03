# models.py   模型，跟数据库相关


from .exts import db

#模型      ：数据库
#类        ：表结构
#类属性     ：表字段
# 一个对象  ：标的一行数据

#模型
#必须继承db.Model
class User(db.Model):
    # 表名
    __tablename__='tb_user'
    # 定义表字段
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True,index=True)
    age=db.Column(db.Integer,default=1)
    sex=db.Column(db.Boolean,default=True)

       # nullable=False  ：是否允许为空
    salary=db.Column(db.Float,default=100000,nullable=False)

 
