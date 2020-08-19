import pytest
from page.basepage import BasePage
from page.index import Index


class TestAddressBook:
    data = BasePage.yaml_load('data/member_manage.data.yaml')

    def setup_class(self):
        self.dx = Index()
        # self.dx.driver.implicitly_wait(3)

    def teardown_class(self):
        self.dx.driver.close()

    @pytest.mark.parametrize('name, acct_id, phone, mail, expect', data['test_add_member'])
    def test_add_member(self, name, acct_id, phone, mail, expect):
        res = self.dx.address_book().member_manage().add_member(name, acct_id, phone, mail)
        assert res == expect

    @pytest.mark.parametrize('name, expect', data['test_delete_member'])
    def test_delete_member(self, name, expect):
        res = self.dx.address_book().member_manage().delete_member('杜宁')
        assert res == expect
