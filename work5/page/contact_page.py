from selenium.webdriver.common.by import By

from page.add_department_page import AddDepartPage
from page.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_add_department(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.find(self.add_department_ele1).click()
        self.find(self.add_department_ele2).click()
        return AddDepartPage(self.driver)

    def get_list(self):
        #
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, "[aria-level='5']")
        name_list = [i.text for i in ele_list]
        # name_list = []
        # for i in ele_list:
        #     name_list.append(i.text)
        # print(name_list)
        return name_list