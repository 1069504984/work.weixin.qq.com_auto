import time
from selenium.webdriver.common.by import By

from common.log import Log
from page.basepage import BasePage


class MemberManage(BasePage):

    def add_member(self, name, acct_id, phone, mail):
        """
        新增成员功能，实现用例的数据驱动
        :param name: 姓名
        :param acct_id: 账号
        :param phone: 手机号
        :param mail: 邮箱  手机号和邮箱填一个就行
        :return:
        """
        time.sleep(2)

        Log().warn('点击添加成员')
        el = self.driver.find_element_by_xpath('//*[text()="添加成员"]')
        self.driver.execute_script("arguments[0].click();", el)  # js点击

        Log().warn('输入成员姓名: {}'.format(name))
        self.find(By.ID, 'username').send_keys(name)

        Log().warn('输入成员账号: {}'.format(acct_id))
        self.find(By.ID, 'memberAdd_acctid').send_keys(acct_id)

        Log().warn('输入成员手机号: {}'.format(phone))
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)

        Log().warn('输入成员邮箱: {}'.format(mail))
        self.find(By.ID, 'memberAdd_mail').send_keys(mail)

        Log().warn('点击保存')
        self.finds(By.XPATH, '//*[text()="保存"]')[0].click()
        time.sleep(3)
        try:
            self.find(By.XPATH, '//*[text()="添加成员"]').text()
            Log().info('返回True')
            return True
        except:
            Log().info('返回False')
            return False

    def delete_member(self, name):
        self.driver.refresh()
        try:
            Log().warn('点击成员: {}'.format(name))
            self.find(By.XPATH, '//*[text()="{}"]'.format(name)).click()
        except:
            print('点击失败')

        Log().warn('点击删除')
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn js_del_member" and text()="删除"]').click()
        self.find(By.XPATH, '//*[text()="确认"]').click()
        try:
            self.find(By.XPATH, '//*[text()="{}"]'.format(name)).text()
            Log().info('返回True')
            return False
        except:
            Log().info('返回False')
            return True

