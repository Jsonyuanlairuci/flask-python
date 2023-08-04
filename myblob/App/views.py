# views.py  理由+视图函数

# 蓝图   是一种规划，主要用来规划urls (路由route)
from flask import Blueprint,request
from .models import *


blue=Blueprint('user',__name__)         #蓝图名称，后面坐反向解析使用·


@blue.route('/')
def index():
    print('1234')
    return 'index'


@blue.route('/request_test/',methods=['GET','POST'])
def get_request():

    #get请求
               #ImmutableMultiDict 类字典对象     可以出现重复的key
    print(request.args)      #获取get请求的参数   ImmutableMultiDict([('name', 'aaaa'), ('name', 'bbb'), ('age', '18')])    允许有重复的key  

    # 获取参数的方式：
    print(request.args['name'],request.args['age'])          #参数名不存在会报错      参数重复则只会获取到第一个
    print(request.args.get('haha'))                          #参数名不存不会报错   会返回None
    print(request.args.getlist('name'))                      #参数名重复时使用    会返回一个列表

    #---------------------------------------------------------
    print(request.form)       #获取post请求的参数   ImmutableMultiDict([('name', 'aaa'), ('name', '王小二'), ('age', '90'), ('sex', 'nan')])     允许有重复的key
    print(request.form.get('name'))                       #post获取参数     同get里面的   request.args.get('haha')  方法
    print(request.method)
    return "request is ok;"

@blue.route('/addUser/',methods=['GET','POST'])
def user_add():
    # 添加一条数据
    # u=User()
    # u.name='luoj'
    # u.age=24
    # db.session.add(u)
    # db.session.commit()


    # 添加多条数据
    users=[]
    for i in range(10,30):
        u=User()
        u.name='测试'+str(i)
        u.age=i
        users.append(u)
    try:
        db.session.add_all(users)
        db.session.commit()      #事务提交
    except  Exception as e:
        db.session.rollback()      #事务回滚
        db.session.flush()         #清空缓存
        return 'fail:'+str(e)
    return 'add user data ok;'

# 删除操作
@blue.route('/delUser/',methods=['GET','POST'])
def user_del():
    u=User.query.first()
    db.session.delete(u)
    db.session.commit()
    return 'del first data is ok;'


# 修改操作
@blue.route('/updateUser/',methods=['GET','POST'])
def update_del():
    u=User.query.first()
    u.name='测试修改第一条数据'
    db.session.commit()
    return 'update first data is ok;'


# 查询操作
@blue.route('/selectUser/',methods=['GET','POST'])
def select_del():
    users=User.query.all()
    print(users)         #数据库列表
    print(User.query)    #SQL语句
    return 'select first data is ok;'