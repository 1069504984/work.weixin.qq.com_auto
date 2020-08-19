import os
import time
import json
from selenium import webdriver


class LoginCookie:
    path = os.path.join(os.path.dirname(__file__), 'cookie.json')

    def get_cookie(self, url):
        # 填写webdriver的保存目录
        # 记得写完整的url 包括http和https
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(20)  # 等待20s。手动登陆后获取cookie
        with open(self.path, 'w') as f:  # 打开文件，如果不存在则创建
            # 将cookies保存为json格式
            f.write(json.dumps(driver.get_cookies()))

    def login_cookie(self, driver):
        # 利用cookie登陆，登陆后刷新页面
        print(self.path)
        with open(self.path, 'r') as f:
            cookies_list = json.load(f)
        for cookie in cookies_list:
            driver.add_cookie(cookie)
        driver.refresh()


if __name__ == '__main__':
    url = 'https://work.weixin.qq.com/wework_admin/frame'
    LoginCookie().get_cookie(url)
