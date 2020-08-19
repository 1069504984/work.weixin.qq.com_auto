from selenium.webdriver.common.by import By

from common.log import Log
from page.address_book.index import AddressBook
from page.application_management.index import ApplicationManagement
from page.basepage import BasePage
from page.customer_contact.index import CustomerContact
from page.home_page.index import HomePage
from page.management_tools.index import ManagementTools
from page.my_company.index import MyCompany


class Index(BasePage):
    """
    登陆后的停留页
    分发driver给各一级菜单，实现case中的链式调用
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def home_page(self):
        return HomePage(self.driver)

    def address_book(self):
        Log().warn('点击通讯录')
        self.find(By.XPATH, '//*[text()="通讯录"]').click()
        return AddressBook(self.driver)

    def application_management(self):
        self.find(By.XPATH, '//*[text()="应用管理"]').click()
        return ApplicationManagement(self.driver)

    def customer_contact(self):
        self.find(By.XPATH, '//*[text()="客户联系"]').click()
        return CustomerContact(self.driver)

    def management_tools(self):
        self.find(By.XPATH, '//*[text()=" 管理工具  "]').click()
        return ManagementTools(self.driver)

    def my_company(self):
        self.find(By.XPATH, '//*[text()="我的企业"]').click()
        return MyCompany(self.driver)
