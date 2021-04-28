from selenium import webdriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.contact_page import ContactPage

class AddDepartPage(BasePage):
    def add_depart(self, name):
        # self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_inputText ww_inputText").send_keys("name")
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body ww_dialog_body [id='1688851151620386_anchor']").click()

        # 点击确定
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn ww_btn ww_btn_Blue").click()
        return ContactPage(self.driver)
