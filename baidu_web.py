'''
基础层BasePage,封装一些常用方法
open()方法用于打开网页
by_id()方法通过id定位
by_name()方法通过name定位
by_class_name()方法通过class_name定位
by_tag_name()方法通过tag标签定位
by_link_text()方法通过文本内容定位
by_partial_link_text()方法通过部分文本内容定位
by_xpath()方法通过xpath定位
by_css()方法通过css定位
get_title()和get_text()方法，是自动化测试经常用到的方法，get_text()方法需要接收元素定位
执行Javascript脚本也是常用到的方法
'''

import time
from selenium import webdriver

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #TODO 打开页面
    def open(self,url=None):
        if url == None:
            self .driver.get(self.url)
        else:
            self.driver.get(url)

    # TODO 封装8种定位元素
    # TODO id定位
    def by_id(self,id):
        return self.driver.find_element_by_id(id)

    # TODO name定位
    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    # TODO class定位,by_class_name()方法通过class_name定位
    def by_class_name(self,class_name):
        return self.driver.find_element_by_class_name(class_name)

    # TODO tag_name定位,by_tag_name()方法通过tag标签定位
    def tag_name(self,tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    # TODO link定位,by_link_text()方法通过文本内容定位
    def by_link_test(self,link_text):
        return self.driver.find_element_by_link_text(link_text)

    # TODO partial link定位,by_partial_link_text()方法通过部分文本内容定位
    def by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    # TODO xpath定位,
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    # TODO css定位
    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    # TODO 获取title
    def get_title(self):
        return self.driver.title

    # TODO 获取页面text,仅使用xpath定位
    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    # TODO 执行js脚本
    def js(self,script):
        self.driver.execute_script(script)
