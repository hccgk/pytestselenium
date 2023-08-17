import pytest
from selenium import webdriver
from utils.configsUtil import configer



class BaseTest(object):
    def __init__(self):
        self.driver = None

    # def __int__(self,driver=None):
    #     if driver is None:
    #         self.driver = webdriver.Chrome()
    #     else:
    #         self.driver = driver
    #     self.driver.implicitly_wait(30)

    # def __del__(self):
    #     print("BaseTest is deleted.")  # 基类方法

    # def setup_class(cls):
    #     print("测试类前置方法---setup_class---")
    #
    # def setup_method(function):
    #     print("测试用例前置方法---setup_method---")
    #
    # def teardown_method(self):
    #     print("测试用例后置方法---teardown_method---")
    #
    # def teardown_class(cls):
    #     print("测试类后置方法---teardown_class---")
    #
    # # -----------------------------
    # def setup_module(module):
    #     print("测试模块的前置方法---setup_module---")
    #
    #
    # def teardown_module(module):
    #     print("测试模块的前置方法---teardown_module---")
    #
    #
    # def setup_function(function):
    #     print("函数用例前置方法执行")
    #
    #
    # def teardown_function(function):
    #     print("函数用例后置方法执行")

    @pytest.fixture()  #scope="session"  function class module package session
    def driver(self):
        self.driver = webdriver.Chrome()
        d = self.driver
        yield d
        d.quit()

    def configNameValue(self,name,thing):
        print(name+thing)
        return configer.nameAndThings(name, thing)