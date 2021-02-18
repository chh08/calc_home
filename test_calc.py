import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:
    # 定义测试方法
    @allure.story("测试加法")
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_datas):
        # 调用add方法
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_datas[0], get_datas[1])
        # 判断result是浮点数，作出保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == get_datas[2]


    @allure.story("测试除法")
    @pytest.mark.div
    @pytest.mark.run(order=2)
    def test_div(self, get_calc, get_datas1):
        #调用通过div方法
        with allure.step("计算两个数相除"):
            result = get_calc.div(get_datas1[0], get_datas1[1])
        # 得到结果之后，需要写断言
        assert result == get_datas1[2]

    @allure.story("测试减法")
    @pytest.mark.sub
    @pytest.mark.run(order=3)
    def test_sub(self, get_calc, get_datas2):
        # 调用通过sub方法
        with allure.step("计算两个数相减"):
            result = get_calc.sub(get_datas2[0], get_datas2[1])
        # 得到结果之后，需要写断言
        assert result == get_datas2[2]

    @allure.story("测试乘法")
    @pytest.mark.mul
    @pytest.mark.run(order=4)
    def test_mul(self, get_calc, get_datas3):
        # 调用通过mul方法
        with allure.step("计算两个数相减"):
            result = get_calc.mul(get_datas3[0], get_datas3[1])
        # 判断result是浮点数，作出保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == get_datas3[2]