# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:39:43 2018

@author: Jarily
"""

answer = [0]*555
re_get = []

titles = set()

cnt = 0

new_url = []

def cal(index):
    fname = 'question/question' + str(index) + '.txt'
    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()
        #print(data)
        ls = data.split("###\n")
        '''
        for l in ls:
            print(l)
            print("**************************")
        '''
        #print(ls)
        qst_str = ls[0]  # 问题部分
        #print(qst_str)
        qst_info = ls[0].split("---\n") 
        qst_comment = qst_info[0].strip().split('\n')  #问题的标记信息 发布时间和回答数量
        #print(len(qst_comment[0]))
        print(qst_comment[0])
        if qst_comment[0] in titles:
            pass
        else:
            titles.add(qst_comment[0])
            global cnt
            fname1 = 'question_cleans/question' + str(cnt) + '.txt'
            cnt = cnt + 1
            new_url.append(url[index])
            with open(fname1, 'w', encoding='utf-8') as f1:
                f1.write('['+url[index]+']\n'+data)
        #print("回答数量：%d  抓取数量：%d" % (ans_num,len(ls)-1))
        #print("抓取数量：%d"%(len(ls)-1))
        #return ans_num, len(ls)-1

url = []
seq = []
title = []        

def init():
    with open("question_url_kw.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        #print(lines)
        for line in lines:
            #print(line)
            s = line.find('@')
            t = line.find('#')
            url.append(line[:s])
            seq.append(int(line[s+1:t]))
            title.append(line[t+1:].strip())
            #print(url)
            #print(seq)
            #print(title)       

def main():
    init()
    #print(url)
    #print(seq)
    #print(title) 
    for i in range(0,555):
        if i !=388:
            cal(i)
            #f1.write(date+'\n')
    global cnt
    print(cnt)
    with open("data_res/new_url.txt", 'w', encoding='utf-8') as f:
        for i in range(0,len(new_url)):
            f.write(new_url[i]+'\n')
   
if __name__ == '__main__':
    main()