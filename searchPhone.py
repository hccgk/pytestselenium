import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.smzdm.com/")
        # ""
        input_key = self.driver.find_element(By.XPATH,'//*[@id="J_search_input"]')
        input_key.send_keys("冰箱",Keys.ENTER)
        time.sleep(3)
        self.assertEqual(self.driver.title, "冰箱_综合_什么值得买")  # add assertion here


if __name__ == '__main__':
    unittest.main()



