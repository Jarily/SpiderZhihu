# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:59:16 2018

@author: Jarily
"""

# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

keywords = [u'天津塘沽爆炸',u'天津港爆炸',u'天津爆炸']

cnt = 0

#知乎的模拟登录
browser = webdriver.Chrome(r"E:\pycode\chromedriver.exe") # 创建实例
browser.get("https://www.zhihu.com/signin")

def login_zhihu(browser):
    try:
        #获取登录用户名
        elem = browser.find_element_by_name("username")
        elem.clear()  # 清空
        elem.send_keys("XXXXXXXXXX")  # 自动填值
        #elem.send_keys(Keys.RETURN)#回车

        time.sleep(3)

        #获取登录密码
        elem = browser.find_element_by_name("password")
        elem.clear()
        elem.send_keys("XXXXXXXXXX")
        #elem.send_keys(Keys.RETURN)#回车

        time.sleep(2)

        print("开始登陆...")
        #Button SignFlow-submitButton Button--primary Button--blue
        elem = browser.find_element_by_css_selector(".Button.SignFlow-submitButton.Button--primary.Button--blue")
        #elem = browser.find_element_by_xpath(r'//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]')
        #print("elem:")
        #print(elem)
        elem.click()

        print("开始休眠...")
        #显示等待   选择“首页”选项
        element = WebDriverWait(browser, 15).until(EC.title_contains(u'首页 - 知乎'))
        print("已选择...")

    except TimeoutException:
        print("Time Out")
    except NoSuchElementException as msg:
        print("No Element -- %s" % msg)

def search(index):
    try:
        #elem = browser.find_element_by_css_selector(".SearchBar-input.Input-wrapper.Input-wrapper--grey")
        #Popover1-toggle
        elem = browser.find_element_by_id("Popover1-toggle")
        time.sleep(3)
        elem.clear()
        time.sleep(3)
        elem.send_keys(keywords[index])
        time.sleep(3)
        #Zi Zi--Search
        elem = browser.find_element_by_class_name("Zi--Search")
        elem.click()
        time.sleep(3)
        #browser.back()
        time.sleep(10)
    except NoSuchElementException as msg:
        try:
            elem = browser.find_element_by_id("Popover2-toggle")
            time.sleep(3)
            elem.clear()
            time.sleep(3)
            elem.send_keys(keywords[index])
            time.sleep(3)
            #Zi Zi--Search
            elem = browser.find_element_by_class_name("Zi--Search")
            elem.click()
            time.sleep(3)
            #browser.back()
            time.sleep(10)
        except NoSuchElementException as msg:
            print("No Element -- %s" % msg)
# url 去重
urls = set()

def get_information(browser):
    
    print("开始获取信息。。。")
    print("\n-----------------")
    f = open('tjbz.txt', 'a',encoding='utf-8') # 以写方式打开
    
    time.sleep(3)
    elems = browser.find_elements_by_css_selector(".ContentItem-title")
    for elem in elems:
        try:
            l_elem = elem.find_element_by_class_name("SearchItem-type")
            print('give up!!!')    
        except NoSuchElementException as msg:
            #print("No Element -- %s" % msg)
            link_elem = elem.find_element_by_tag_name("a")
            if link_elem.get_attribute("href") in urls:
                pass
            else:
                global cnt
                print("NO. %d" % cnt)
                f.write("[NO. " + str(cnt)+"] ")
                cnt = cnt + 1
                print(link_elem.text)  # 标题
                f.write(link_elem.text + "\n")
                f.write(link_elem.get_attribute("href")+"\n\n")
                print(link_elem.get_attribute("href"))  # 链接
                print("---")
                #link_elem.click()
                #time.sleep(3)
                #browser.back()
                urls.add(link_elem.get_attribute("href"))
            
        #link_elem = elem.find_element_by_tag_name("a")
    print("-----------------\n")
    f.close()
        
        #if link_elem.text in urls:
        #    pass
        #else:
        #    print(link_elem.text)  # 标题
        #    print(link_elem.get_attribute("href"))  # 链接
            #link_elem.click()
            #time.sleep(3)
            #browser.back()
        #    urls.add(link_elem.get_attribute("href"))
            
# 滚动加载
def scroll_load(browser):
    #利用 execute_script() 方法将进度条下拉到最底部
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.implicitly_wait(10)  # 隐式等待


def scroll_load_top(browser):
    #利用 execute_script() 方法将进度条下拉到最底部
    browser.execute_script("window.scrollTo(0, 0);")
    browser.implicitly_wait(10)  # 隐式等待

# 主主函数
def main():
    #global cnt
    #cnt = 0
    login_zhihu(browser)  # 登录函数
    for index in range(0,3):
        time.sleep(10)
        scroll_load_top(browser)
        time.sleep(10)
        search(index)
        time.sleep(5)
        
        for i in range(20):  #滚动三次
            #get_information(browser)  # 获取标题与链接
            #search()
            scroll_load(browser)  # 滚动
            time.sleep(2)  # 休眠
        get_information(browser)  # 获取标题与链接        
        
# 函数入口调用
if __name__ == '__main__':
    #login_zhihu(browser)  # 登录函数
    #search()
    #get_information(browser)  # 获取标题与链接
    main()

    input("按任意键退出-> ")
    browser.quit()
