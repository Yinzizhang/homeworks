import pytest

from Calculator import Calculator


@pytest.fixture()
def calculate():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")
