# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:12:35 2018

@author: Jarily
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re

browser = webdriver.Chrome(r"E:\pycode\chromedriver.exe") # 创建实例

urls = []

def login_zhihu():
    browser.get("https://www.zhihu.com/signin")
    try:
        #获取登录用户名
        elem = browser.find_element_by_name("username")
        elem.clear()  # 清空
        elem.send_keys("***********")  # 自动填值
        #elem.send_keys(Keys.RETURN)#回车

        time.sleep(3)

        #获取登录密码
        elem = browser.find_element_by_name("password")
        elem.clear()
        elem.send_keys("***********")
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


def get_usr(index, url):
    time.sleep(2)
    browser.get(url) 
    print("开始获取信息......")
    try:
        #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
        # //*[@class='zm-item']/div[position()=1]/a[position()=1]
        #elem = browser.find_element_by_xpath("/html/body/div[position()=3]/div[position()=1]/div/div[position()=3]/div[position()=3]/div[position()=1]/a[position()=1]")
        # //*[@id='logitem-1232332327']/div[position()=1]/a[position()=1]
        elem = browser.find_element_by_xpath("//*[@class='zm-item'][last()]/div[position()=1]/a[position()=1]")
        #elem = browser.find_element_by_xpath("//*[@class='zhi ']")
        print(elem.text)
        return elem.text
    except NoSuchElementException as msg:
            print("用户抓取失败 -- %s" % msg)
            return ""


def get_new_url():
    with open("data_res/new_url.txt", 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        for line in lines:
            line = line.strip()
            s = line.find("/answer")
            if s == -1:
                line = line + '/log'
            else:
                line = line[:s] + '/log'
            urls.append(line)
        
def main():
    get_new_url()
    #print(urls)
    
    login_zhihu()
    n = 519
    
    #for i in range(0,4):
    with open("data_res/question_usr.txt", 'a', encoding='utf-8') as f1:
        for i in range(194, n):
            #url = get_url(qst[re_get[i]])
            print('\n############################################################################\n正在抓取第%d个问题...... %s'%(i, urls[i]))
            data = get_usr(i, urls[i])
            if data!="":
                f1.write(data+'\n')
            else:
                print("error!!!!")
                break
            time.sleep(2)
        print("done!")
    
   # browser.get("https://www.zhihu.com/question/34797486")
   # time.sleep(5)
   # browser.get("https://www.zhihu.com/question/34535765")
  
    
# 函数入口调用
if __name__ == '__main__':
    main()


