import pytest


# 创建fixture方法
@pytest.fixture()
def login():
    print("登录操作")
    username = 'python'
    password = 'Abc123456'
    token = '123456'
    yield [username, password, token]
    print("登出操作")


def test1(login):
    print("测试用例1")
    print(f"登录信息是：{login}")


def test2():
    print("测试用例2")


def test3(login):
    print("测试用例3")


@pytest.mark.usefixtures("login")
def test4():
    print("测试用例4")
