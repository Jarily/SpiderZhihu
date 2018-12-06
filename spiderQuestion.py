# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:15:47 2018

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

qst = []
urls = set()
cnt = 0

re_get = [359, 361, 363, 364, 366, 367, 368, 381, 412, 417, 422, 430, 431, 434, 446, 448, 462, 471, 483, 496, 497, 499, 541]

def login_zhihu():
    browser.get("https://www.zhihu.com/signin")
    try:
        #获取登录用户名
        elem = browser.find_element_by_name("username")
        elem.clear()  # 清空
        elem.send_keys("**********")  # 自动填值
        #elem.send_keys(Keys.RETURN)#回车

        time.sleep(3)

        #获取登录密码
        elem = browser.find_element_by_name("password")
        elem.clear()
        elem.send_keys("**********")
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

def init():
    with open('all_question.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        tmp = []
        for line in lines:
            if 'https://www.zhihu.com/question' in line:
                ls = line.strip()
                if ls in urls:
                    pass
                else:
                    #qst.append(ls)
                    #print(tmp)
                    s = tmp.find('[')
                    t = tmp.find(']')
                    tmp = tmp[t+2 : ]
                    tmp = tmp.strip()
                    #print(tmp)
                    #print(ls)
                    global cnt
                    qst.append(ls+'@'+str(cnt)+'#'+tmp)
                    cnt = cnt + 1
                    urls.add(ls)
            tmp = line
        #global qst
        #qst = list(set(qst_url))  #去重
        
    with open('question_url_kw.txt', 'w', encoding='utf-8') as f:
        for q in qst:
            f.write(q + '\n')

def get_url(data):
    s = data.find('/answer')
    t = data.find('@')
    if s == -1:
        #print(data[:t])
        return data[:t]
    else:
        return data[:s]

# 滚动加载
def scroll_load(browser, lens, wait):
    #利用 execute_script() 方法将进度条下拉到最底部
    for i in range(lens):  #滚动
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait)  # 休眠
        #browser.implicitly_wait(wait)  # 隐式等待
        if i%5 == 0:
            browser.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            #browser.implicitly_wait(1)  # 隐式等待
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    
def acc():
    time.sleep(10)
    # 抓取 问题的回答数量
    try:
        #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
        elem = browser.find_element_by_xpath("/html/body/div[position()=1]/div/main[position()=1]/div/meta[@itemprop=\"answerCount\"]")
        #print(elem.get_attribute("content"))
        ans_num = int(elem.get_attribute("content"))
        if ans_num <= 15:
            return 1
        else:
            return 0
        #print("回答数量：%d" % ans_num)
        #f.write("回答数量：" + str(ans_num) + '\n')
        #f.write(elem.text+'\n')
    except NoSuchElementException as msg:
        print("问题回答数量抓取失败 -- %s" % msg)
        return 1


def get_data(index, url):
    browser.get(url)
    time.sleep(10)
    scroll_load(browser,30,2)  # 滚动
    
    #res = acc()
    #if res == 1:
    #    scroll_load(browser,10,5) 
    #else:
    #    scroll_load(browser,20,5) 
    
    print("开始获取信息......")
    fname = 'question/question' + str(index) + '.txt'
    with open(fname, 'w', encoding='utf-8') as f:
        ans_num = 0
        # 抓取标题
        try:
            #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
            elem = browser.find_element_by_xpath("/html/body/div[position()=1]/div/main[position()=1]/div/div[position()=1]/div[position()=2]/div[position()=1]/div[position()=1]/h1[position()=1]")
            print(elem.text)
            f.write(elem.text+'\n')
        except NoSuchElementException as msg:
            print("标题抓取失败 -- %s" % msg)
            
        # 抓取 问题补充
        try:
            #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
            elem = browser.find_element_by_xpath("/html/body/div[position()=1]/div/main[position()=1]/div/div[position()=1]/div[position()=2]/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div/span")
            print(elem.text)
            f.write(elem.text+'\n')
        except NoSuchElementException as msg:
            print("问题补充抓取失败 -- %s" % msg)
            
        # 抓取 问题发布时间
        try:
            #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
            elem = browser.find_element_by_xpath("/html/body/div[position()=1]/div/main[position()=1]/div/meta[@itemprop=\"dateCreated\"]")
            #print(elem.get_attribute("content"))
            tt = re.findall(r"\d+\.?\d*", elem.get_attribute("content"))
            qst_time =str(tt[0]+'-'+tt[1]+'-'+tt[2])
            print("---\n发布时间：%s" % qst_time)
            f.write("---\n发布时间：" + qst_time + '\n')
            #f.write(elem.text+'\n')
        except NoSuchElementException as msg:
            print("问题发布时间抓取失败 -- %s" % msg)
        # 抓取 问题的发起人
        # 抓取 问题的回答数量
        try:
            #find_element_by_css_selector  find_element_by_class_name  find_element_by_xpath
            elem = browser.find_element_by_xpath("/html/body/div[position()=1]/div/main[position()=1]/div/meta[@itemprop=\"answerCount\"]")
            #print(elem.get_attribute("content"))
            ans_num = int(elem.get_attribute("content"))
            print("回答数量：%d" % ans_num)
            f.write("回答数量：" + str(ans_num) + '\n')
            #f.write(elem.text+'\n')
        except NoSuchElementException as msg:
            print("问题回答数量抓取失败 -- %s" % msg)
        #//*[@class='RichContent-inner']
        #ContentItem AnswerItem
        # 抓取所有答案
        try:
            elems = browser.find_elements_by_css_selector(".ContentItem.AnswerItem")
            case = 1
            for elem in elems:
                #print(elem.text)
                print("\n###\n")
                f.write("\n###\n")      
                # 抓取 回答内容
                try:
                    l_elem = elem.find_element_by_class_name("RichContent-inner")
                    print(l_elem.text)
                    f.write(l_elem.text + '\n')
                except NoSuchElementException as msg:
                    print("回答内容抓取失败 -- %s" % msg)
                
                print("---\n回答序列：%s" % case)
                f.write("---\n回答序列：" + str(case) + '\n')
                # 抓取 回答时间
                try:
                    l_elem = elem.find_element_by_class_name("ContentItem-time")
                    tt = re.findall(r"\d+\.?\d*", l_elem.text)
                    ans_time =str(tt[0]+'-'+tt[1]+'-'+tt[2])
                    print("回答时间：%s" % ans_time)
                    f.write("回答时间：" + ans_time + '\n')
                except NoSuchElementException as msg:
                    print("回答时间抓取失败 -- %s" % msg)
                
                # 抓取 回答用户
                try:
                    l_elem = elem.find_element_by_class_name("AuthorInfo-content")
                    try:
                        link_elem = l_elem.find_element_by_class_name("UserLink-link")
                        print("回答用户：%s" % link_elem.text)
                        f.write("回答用户：" + link_elem.text + '\n')
                    except NoSuchElementException as msg:   
                        print("回答用户：匿名用户")
                        f.write("回答用户：匿名用户\n")
                except NoSuchElementException as msg:
                    print("回答用户抓取失败 -- %s" % msg)

                # 抓取 点赞数
                try:
                    l_elem = elem.find_element_by_css_selector(".Button.VoteButton.VoteButton--up")
                    tt = re.findall(r"\d+\.?\d*", l_elem.text)
                    zan = 0
                    if len(tt)>0:
                        if 'K' in l_elem.text:
                            zan = int(float(tt[0])*1000)
                        else:
                            zan = int(tt[0])
                    print("点赞数量：%d" % zan)
                    f.write("点赞数量：" + str(zan) + '\n')
                except NoSuchElementException as msg:
                    print("点赞数量抓取失败 -- %s" % msg)                    
                case = case + 1

        except NoSuchElementException as msg:
            print("没有回答或者回答抓取失败  实际共有%d条回答-- %s" % (ans_num,msg))
        #elems = browser.find_elements_by_xpath("//*[@class='RichContent-inner']")
        #//*[@class='ContentItem-time']/a/span
        #for elem in elems:
        #    print(elem.text)
        #for i in range(0, ans_num):
            # 抓取 每一条回答的内容
            
            # 抓取 每一条回答的用户
            # 抓取 每一条回答的时间
            # 抓取 每一条回答的点赞数量
def main():
    init()
    login_zhihu()
    #for i in range(0,4):
    # 13 117 重定向
    '''
    tmp = 3
    url = get_url(qst[tmp])
    print('\n############################################################################\n正在抓取第%d个问题...... %s'%(tmp,qst[tmp]))
    get_data(tmp, url)
    '''
    for i in range(0,len(re_get)):
        url = get_url(qst[re_get[i]])
        print('\n############################################################################\n第%d次重新抓取,正在抓取第%d个问题...... %s'%(i,re_get[i],qst[re_get[i]]))
        get_data(re_get[i], url)
        time.sleep(5)
    print(len(re_get))
    #'''
   # browser.get("https://www.zhihu.com/question/34797486")
   # time.sleep(5)
   # browser.get("https://www.zhihu.com/question/34535765")
    
# 函数入口调用
if __name__ == '__main__':
    main()

