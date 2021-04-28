import pytest

from page.contact_page import ContactPage
from page.main_page import MainPage

class TestAddDepart:
    def setup_class(self):
        self.contact = ContactPage()

    @pytest.mark.parametrize("name", ["四级部门"])
    def test_add_department(self, name):
        """
        用来测试添加成员功能
        :return:
        """
        #    1. 跳转到添加成员页面 2. 添加成员 3. 获取成员列表，做断言验证
                    # AddMemberPage()
        # res = self.main.goto_add_department().add_member(name).get_list()

        res = self.contact.goto_add_department().add_depart(name).get_list()
        assert name in res

