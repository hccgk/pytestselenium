import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.base.BaseTest import BaseTest

if __name__ == '__main__':
    pytest.main(['-s','--html=.../report/smzdm_report.html'])


class TestMZDM():
    driver = None
    # def __init__(self):
    #     self.driver = None
    #
    def setup(self):
        print("预置条件，和重置环境要成对出现;方法前执行---setup---")

    def teardown(self):
        print("重置环境；方法后执行---teardown---")
        self.driver.find_element(By.ID, 'logo').click()
        print("click logo")
        time.sleep(2)

    def setup_class(self):
        print("测试类前置方法---setup_class---")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.smzdm.com")

    def teardown_class(self):
        print("测试类后置方法 ;也有叫重置条件---teardown_class---")
        self.driver.quit()

    # @pytest.mark.parametrize('args', [1, 2, 3])
    # @pytest.mark.smoke
    # def test_xyz_args(self, args):
    #     print(args)
    #
    # @pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
    # def test_multiply_by_two(self,input, expected):
    #     assert input * 2 == expected
    #
    # @pytest.mark.parametrize('args', 'dd')
    # def test_xyz_args(self, args):
    #     print(args)

    def test_01search_phone(self):
        driver = self.driver
        print(driver.title)
        input_key = self.driver.find_element(By.XPATH, '//*[@id="J_search_input"]')
        input_key.send_keys("手机", Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="feed-main"]/div[2]/div[1]/a/span').click()
        print(self.driver.find_element(By.XPATH,'//*[@id="feed-main-list"]/li[1]/div/div[2]/div[2]').text)
        assert driver.title == "手机_综合_什么值得买"

    def test_02search_tv(self):
        driver = self.driver
        input_key = self.driver.find_element(By.XPATH, '//*[@id="J_search_input"]')
        input_key.send_keys("电视", Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="feed-main"]/div[2]/div[1]/a/span').click()
        print(self.driver.find_element(By.XPATH, '//*[@id="feed-main-list"]/li[1]/div/div[2]/div[2]').text)
        assert driver.title == "电视_综合_什么值得买"

    def test_04search_bike(self):
        driver = self.driver
        input_key = self.driver.find_element(By.XPATH, '//*[@id="J_search_input"]')
        input_key.send_keys("电动自行车", Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="feed-main"]/div[2]/div[1]/a/span').click()
        print(self.driver.find_element(By.XPATH, '//*[@id="feed-main-list"]/li[1]/div/div[2]/div[2]').text)
        assert driver.title == "电动自行车_综合_什么值得买"

    # def test_muniu(self):
    #     url = "https://muniucloud.lol/user"
    #     print(url)
    #
    #     # // *[ @ id = "email"]
    #     # //*[@id="password"]
    #     # //*[@id="login_submit"]
    #     # //*[@id="crisp-chatbox"]/div/a/span[2]
    #
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(30)
    #     driver.get(url)
    #     time.sleep(5)
    #     driver.find_element(By.XPATH,'//*[ @ id = "email"]').send_keys("")
    #     driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("")
    #     driver.find_element(By.XPATH,'//*[@id="login_submit"]').click()
    #     time.sleep(5)
    #     used_Total =driver.find_element(By.XPATH,'//*[@id="kt_content"]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div')
    #     print(used_Total.text)
    #     outTime = driver.find_element(By.XPATH,'//*[@id="kt_content"]/div[2]/div/div[2]/div[1]/div/div[2]/p')
    #     print(outTime.text)
    #     signButton = driver.find_element(By.XPATH,'//*[@id="checkin"]')
    #     signButton.click()
    #     # time.sleep(300)


