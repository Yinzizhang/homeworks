import time

from selenium import webdriver
from selenium.webdriver.common.by import By


from page.basepage import BasePage


class MainPage(BasePage):
    # 元素定位封装成了一个元祖
    add_department_ele1 = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    add_department_ele2 = (By.CSS_SELECTOR, ".js_create_party")



    def goto_contact(self):
        pass


    def demo(self):
        """
        解元祖示例
        :return:
        """
        a = (1,2) # 1,2
        self.demo2(*a) # = demo2(1,2)

    def demo2(self, a, b):
        print(a, b)