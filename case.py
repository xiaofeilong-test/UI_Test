import unittest

from time import sleep
from selenium import webdriver
from baidu_page import BaiduPage

class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    #搜索功能测试
    def test01(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input('selenium')
        page.search_button()
        sleep(3)
        self.assertEqual(page.get_title(),"selenium_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()