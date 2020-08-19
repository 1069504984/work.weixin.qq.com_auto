from selenium.webdriver.common.by import By

from page.basepage import BasePage


class HomePage(BasePage):

    def add_member(self):
        self.find(By.XPATH, '//*[text()="添加成员"]').click()
        return
