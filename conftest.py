import os
import pytest
import yaml


import sys

from calc import calculator

sys.path.append(os.path.dirname(__file__))


# 使用fixture方法，get_calc实例化calcutator
# 设置scope='module'
@pytest.fixture(scope='module')
def get_calc():
    print("获取计算器实例")
    calc = calculator()
    return calc


# 获取yaml文件数据
with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    # 获取add数据
    add_datas = datas['datas']
    myid = datas['myid']
    # 获取div数据
    div_datas = datas['datas1']
    myid1 = datas['myid1']
    # 获取sub数据
    sub_datas = datas['datas2']
    myid2 = datas['myid2']
    # 获取mul数据
    mul_datas = datas['datas3']
    myid3 = datas['myid3']


# 使用fixture参数化，get_datas获取列表数据
@pytest.fixture(params=add_datas, ids=myid)
def get_datas(request):
    # 执行用例前打印‘开始计算’
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    # yield返回data,执行用例之后打印‘计算结束’
    yield data
    print("计算结束")


# 使用fixture参数化，get_datas获取列表数据
@pytest.fixture(params=div_datas, ids=myid1)
def get_datas1(request):
    # 执行用例前打印‘开始计算’
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    # yield返回data,执行用例之后打印‘计算结束’
    yield data
    print("计算结束")


# 使用fixture参数化，get_datas获取列表数据
@pytest.fixture(params=sub_datas, ids=myid2)
def get_datas2(request):
    # 执行用例前打印‘开始计算’
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    # yield返回data,执行用例之后打印‘计算结束’
    yield data
    print("计算结束")


# 使用fixture参数化，get_datas获取列表数据
@pytest.fixture(params=mul_datas, ids=myid3)
def get_datas3(request):
    # 执行用例前打印‘开始计算’
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    # yield返回data,执行用例之后打印‘计算结束’
    yield data
    print("计算结束")