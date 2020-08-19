from selenium.webdriver.common.by import By
from page.address_book.member_manage import MemberManage
from page.address_book.department_manage import DepartmentManager
from page.address_book.import_member import ImportMember
from page.basepage import BasePage


class AddressBook(BasePage):
    """
    一级菜单
    接收到driver之后，把driver分发给二级菜单或功能
    """
    def member_manage(self):
        # 成员相关操作，增删改查
        return MemberManage(self.driver)

    def department_manager(self):
        # 部门相关的功能
        return DepartmentManager(self.driver)

    def import_member(self):
        # 批量导入成员
        self.find(By.XPATH, '//*[text()="批量导入/导出"]').click()
        return ImportMember(self.driver)