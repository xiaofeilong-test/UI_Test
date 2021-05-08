'''
PO层：封装百度页面元素定位，元素对象以及页面操作
'''

from baidu_web import BasePage

class BaiduPage(BasePage):
    url="http://www.baidu.com"

    #定位搜索框输入搜索数据
    def search_input(self,search_key):
        self.by_id('kw').send_keys(search_key)

    #点击百度搜索按钮
    def search_button(self):
        self.by_id('su').click()
