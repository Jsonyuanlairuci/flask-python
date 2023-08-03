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
