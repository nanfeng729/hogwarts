import pytest
import allure


# @allure.feature("类外面的测试用例")
# def test_a():
#     print('测试用例a')


@allure.feature("计算器计算")
class TestCalc:

    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = calculator()

    # def teardown_class(self):
    #     print("计算结束")

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 2, 3), (0.1, 0.1, 0.2), (-1, -1, -2), (0.1, 0.2, 0.3)],
                             ids=['int', 'float', 'negative', 'round'])
    @allure.story("测试加法")
    def test_add(self, get_calc, a, b, expect):
        # calc = calculator()
        result = get_calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # def test_add2(self):
    #     # calc = calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
    #
    # def test_add3(self):
    #     # calc = calculator()
    #     result = self.calc.add(-1, -1)
    #     assert result == -2
    @allure.story("测试减法")
    @pytest.mark.parametrize("a,b,expect", [(1, 1, 0), (0, 1, -1), (0, 0, 0), (0.2, 0.1, 0.1), (-1, -2, 1)])
    def test_sub(self, a, b, expect, get_calc):
        result = get_calc.sub(a, b)
        assert result == expect

    @allure.story("测试乘法")
    @pytest.mark.parametrize("a,b,expect",
                             [(1, 0, 0), (0, 1, 0), (0, 0, 0), (1, 1, 1), (0.1, 0.1, 0.01), (-1, 2, -2), (-1, -2, 2)])
    def test_mul(self, a, b, expect, get_calc):
        result = get_calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [(2, 2, 1), (0, 1, 0), (1, 0, '除数不能为0')])
    @allure.story("测试除法")
    def test_chufa(self, a, b, expect, get_calc):
        result = get_calc.div(a, b)
        assert result == expect
