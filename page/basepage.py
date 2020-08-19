import random
import re
import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.get_cookie import LoginCookie


class BasePage:
    _base_url = ""
    driver = None

    def __init__(self, driver: WebDriver = None):
        """
        driver的封装
        :param driver:
        """
        if driver is None:
            # login_page页面会使用这个
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        else:
            # 其他页面需要用这个方法
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)
            LoginCookie().login_cookie(self.driver)


    @classmethod
    def yaml_load(cls, path):
        """
        封装yaml文件的解析
        :param path: yaml文件路径
        :return:python对象
        """
        with open(path, encoding='UTF-8') as f:
            return yaml.safe_load(f)

    def find(self, by, locator):
        """
        定位方法及显示等待的封装
        :param by: 定位方法 如 By.CSS_SELECTOR
        :param locator: 定位元素
        :return:
        """
        el = (by, locator)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(el))
            return self.driver.find_element(by, locator)
        except TimeoutException:
            print('没找到元素，超时')

    def finds(self, by, locator):
        """
        定位方法及显示等待的封装
        :param by: 定位方法 如 By.CSS_SELECTOR
        :param locator: 定位元素
        :return:
        """
        el = (by, locator)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(el))
        return self.driver.find_elements(by, locator)

    def set_records(self, css):
        """
        re 正则模块 返回记录总条数
        :param css: 定位
        :return: 总条数 int
        """
        ob = self.driver.find_element(By.CSS_SELECTOR, css).text
        res = re.search(r'共(.*)条', ob)
        return res.group(1)

    @classmethod
    def mobile(cls):
        # 随机生成122开头手机号
        mobile = '122' + ''.join(random.choice("0123456789") for i in range(8))
        return mobile