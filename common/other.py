import configparser

class Tool:

    def get_config(self, path, name):
        """
        配置文件读取
        todo 移动到action
        :param path: 路径
        :param name: section名
        :return: 该section下的所有键值对
        """
        cf = configparser.ConfigParser()
        cf.read(path, encoding='utf8')  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
        # secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置)
        # host = cf.get(name, 'host')  # 获取host
        items = dict(cf.items(name))  # 获取section名为Mysql-Database所对应的全部键值对
        return items