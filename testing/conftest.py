from python_code.calc import calculator
import pytest


@pytest.fixture(scope='class')
def get_calc():
    print("开始计算")
    calc = calculator()
    # yield calc
    # print("计算结束")
    return calc
