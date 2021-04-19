import allure
import pytest
import yaml

def get_datas():
    with open("./datas/calculator.yml")as f:
        datas = yaml.safe_load(f)
    return datas

@allure.feature("测试计算器")
class TestCal:
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'])
    @allure.story("测试int型相加功能")
    def test_add_int(self,calculate,a,b,expect):
        assert expect == calculate.add(a,b)


    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'],ids=get_datas()['add_float']['ids'])
    @allure.story("测试float型相加功能")
    def test_add_float(self,calculate,a,b,expect):
        assert expect == round(calculate.add(a,b),3)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_int']['datas'])
    @allure.story("测试int型相除功能")
    def test_div_int(self,calculate,a,b,expect):

        assert expect == calculate.div(a,b)


    @pytest.mark.parametrize('a,b,expect', get_datas()['div_float']['datas'],ids=get_datas()['div_float']['ids'])
    @allure.story("测试float型相除功能")
    def test_div_float(self,calculate,a,b,expect):
        assert expect == round(calculate.div(a,b),3)


