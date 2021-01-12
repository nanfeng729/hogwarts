import pytest


# @pytest.fixture()
def provide():
    for i in range(10):
        print("开始操作")
        yield i
        print("结束操作")


p = provide()
print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
