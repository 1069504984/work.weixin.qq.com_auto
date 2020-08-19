import pytest
from page.basepage import BasePage
from page.index import Index


class TestDepartmentManage:
    data = BasePage.yaml_load('../data/department_manage.data.yaml')

    def setup_class(self):
        self.dx = Index()

    def teardown_class(self):
        self.dx.driver.close()

    @pytest.mark.parametrize('name, p_name, expect', data['test_add_dept'])
    def test_add_dept(self, name, p_name, expect):
        res = self.dx.address_book().department_manager().add_dept(name, p_name)
        assert res == expect

    @pytest.mark.skip(reason="不执行该用例")
    @pytest.mark.parametrize('name, expect', data['test_delete_dept'])
    def test_delete_dept(self, name, expect):
        res = self.dx.address_book().department_manager().delete_dept(name)
        assert res == expect
