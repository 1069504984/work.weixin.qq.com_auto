# python UI自动化测试框架
## 简单介绍
环境Windows、python3.x、pytest、selenium、allure2

各模块简单介绍：

    common：封装公共功能
    page：存放页面操作流程，PO设计
    data：存放数据驱动文件，yaml格式
    report：存放测试报告及日志
    testcase：用例
    run.py：执行用例集并生成报告
    
## PO设计及driver传递
提起PO，常挂在嘴边的就是“一个页面封装成一个类”，一开始我是一个case的所有操作全部放在
一个类中（从登陆到case结束），因为如果“一个页面封装成一个类”，执行case时driver会被
实例化多次，后来知道可以通过 return xxx(self.driver)来传递driver，才实现了case中
的链式调用，真正封装好框架。

我是这么设计PO的:
~~~
page：
    base_page.py，封装所有页面的父类BasePage，driver，单例模式
    index.py，用于登陆后driver的分发，将driver分发到各一级菜单
    home_page，一级菜单”首页“:
        index.py，接收分发的driver，并将driver分发给二级菜单或功能
    address_book，一级菜单“通讯录”：
        index.py，接收分发的driver，并将driver分发给二级菜单或功能
        member_manage.py，二级菜单或功能，封装了操作步骤，case的最后一步
~~~

## 数据驱动
跟接口测试框架相似，将功能写在yaml文件，减少页面类中需要维护的代码量。
通过读取yaml文件的数据来驱动，yaml文件中只需要写定位方法和值，
封装好的方法会读取yaml文件后进行操作。

yaml文件格式如下:
```yaml
add_member:
  - {by: XPATH, local: //*[test()='添加成员'], action: click}
  - {by: ID, local: username, action: send_keys, name: ${name}}
  - {by: ID, local: memberAdd_acctid, action: send_keys, acct_id: ${acct_id}}
  - {by: ID, local: memberAdd_phone, action: send_keys, phone: ${phone}}
  - {by: ID, local: memberAdd_mai, action: send_keys, mail: ${mail}}
  - {by: XPATH, local: //*[text()="保存"], action: click}
```


代码更新中 2020.08.19