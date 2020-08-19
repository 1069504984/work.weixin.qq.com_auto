from selenium.webdriver.common.by import By

from page.basepage import BasePage


class DepartmentManager(BasePage):

    def add_dept(self, name, p_name):
        self.find(By.CSS_SELECTOR, 'i.member_colLeft_top_addBtn').click()
        self.find(By.XPATH, '//*[text()= "添加部门"]').click()
        self.find(By.NAME, 'name').send_keys(name)
        if p_name:
            self.find(By.CSS_SELECTOR, 'a.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list').click()
            self.finds(By.XPATH, '//a[text()= "{}"]'.format(p_name))[1].click()
        self.find(By.XPATH, '//*[text()= "确定"]').click()

        try:
            self.finds(By.XPATH, '//a[text()= "{}"]'.format(name))[0].click()
            return True
        except:
            return False

    def delete_dept(self, name):
        self.find(By.XPATH, '//a[text()="{}"]/./span'.format(name)).click()  # todo 就是这里
        self.find(By.XPATH, '//a[text()="删除"]').click()
        self.find(By.XPATH, '//a[text()="确定"]').click()

        try:
            self.finds(By.XPATH, '//a[text()= "{}"]'.format(name))[0].click()
            return False
        except:
            return True
