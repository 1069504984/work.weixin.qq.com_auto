import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.get_cookie import LoginCookie
from common.log import Log


class BasePage:
    _base_url = ""
    params = {}
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
            # 使用cookie登陆，调试时也可复用ChromeOption达到验证登陆的目的
            # options = webdriver.ChromeOptions()
            # options.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=options)
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

    def steps(self, steps: list):
        element = None
        for step in steps:
            # print(step)
            if "by" in step.keys():
                # if step["by"] == 'XPATH':
                #     element = self.find(By.XPATH, step["local"])
                element = self.find(eval(step['by']), step["local"])

            if "action" in step.keys():
                action = step["action"]
                if action == 'click':
                    element.click()
                elif action == 'text':
                    element.text
                elif action == 'attribute':
                    element.get_attribute(step['value'])

                elif action == 'send_keys':
                    # print(step)
                    # print('action到了')
                    # print(self.params.keys())
                    for key in self.params.keys():
                        # print('key:', key)
                        if key in step:
                            # print('key in step:')
                            content = step[key].replace("${%s}" % key, self.params[key])  # 参数替换
                            print('content:', content)
                            element.send_keys(repr(content))
