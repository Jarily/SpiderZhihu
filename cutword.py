# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:51:05 2018

@author: Jarily
"""


import jieba
import jieba.posseg as psg
#ss = " # ".join(jieba.cut(ss))
#print([(x.word,x.flag) for x in psg.cut(ss)])

# hehe =[(x.word,x.flag) for x in psg.cut(ss) if x.flag.startswith('n')]  #只要名词
hehe =[x.word for x in psg.cut(ss) if x.flag.startswith('n') or x.flag.startswith('v')]  #只要名词
#print(ss)

from collections import Counter
#c = Counter(hehe).most_common(20)
#print(c)

kw = ['爆炸','救援','撤离','调查','追责','居民','瑞海','媒体','市政府','消防','公安','安监局','环保局','环境','污染','空气','废水','化学品','氰','环评']

def get_answer_data(index,k):
    fname = 'question_clean/question' + str(index) + '.txt'
    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()
        #print(data)
        ls = data.split("###\n")
        
        kk = 0
        res = ''
        
        if len(ls) == 1: #没有回答
            return res         
        
        for i in range(1,len(ls)):
            #print(i)
            ans_info = ls[i].strip().split("---\n")
            if kw[k] in ans_info[0]:
                res = res + ans_info[0]
        return res

def main():
    n = 519
    with open("data_res/kw_associated_frequency.txt", 'w', encoding='utf-8') as f1:
        f1.write("关键词关联词汇  出现频次"+'\n'+'----------------\n')
        for k in range(0,len(kw)): #len(kw)):
            print("处理第%d个关键字：%s"%(k, kw[k]))
            f1.write("\n关键字 ["+ kw[k]+"] 的关联词汇以及出现频次\n----------------------------\n")
            kres = ''
            for i in range(0, n):
                kres += get_answer_data(i,k)
                #print("处理第%d组数据"%i)
            #print(kres)
            #hehe =[x.word for x in psg.cut(kres) if x.flag.startswith('n') or x.flag.startswith('a') or x.flag.startswith('d') ] 
            minci = [x.word for x in psg.cut(kres) if x.flag.startswith('n') and len(x.word)>1]
            c = Counter(minci).most_common(30)
            f1.write("名词前30频次\n")    
            for  j in range(0, len(c)):
                if j%5 == 0:
                    f1.write("\n")
                f1.write("("+c[j][0]+", "+str(c[j][1])+") ")
            f1.write("\n\n")
            f1.write("动词前30频次\n")
            dongci = [x.word for x in psg.cut(kres) if x.flag.startswith('v') and len(x.word)>1]
            c = Counter(dongci).most_common(30)
            print(c)
            for  j in range(0, len(c)):
                if j%5 == 0:
                    f1.write("\n")
                f1.write("("+c[j][0]+", "+str(c[j][1])+") ")
            f1.write("\n\n")
            f1.write("形容词前30频次\n")
            adj = [x.word for x in psg.cut(kres) if x.flag.startswith('a') and len(x.word)>1]
            c = Counter(adj).most_common(30)
            for  j in range(0, len(c)):
                if j%5 == 0:
                    f1.write("\n")
                f1.write("("+c[j][0]+", "+str(c[j][1])+") ")
            f1.write("\n\n")
            
            f1.write("副词前30频次\n")
            adv = [x.word for x in psg.cut(kres) if x.flag.startswith('d') and len(x.word)>1]
            c = Counter(adv).most_common(30)
            for  j in range(0, len(c)):
                if j%5 == 0:
                    f1.write("\n")
                f1.write("("+c[j][0]+", "+str(c[j][1])+") ")
            f1.write("\n\n\n\n")
            
            #f1.write(str(c))
            #kkw = kw[k]
            #for j in range(len(kw[k]),10):
            #    kkw = kkw + ' '
            #f1.write(kkw+str(kcnt)+'\n')   

if __name__ == '__main__':
    main()
    #hehe =[x.word for x in psg.cut(ss) if x.flag.startswith('n') or x.flag.startswith('v')]  #只要名词
    #c = Counter(hehe).most_common(20)
    #print(c)
    #for i in c:
    #    print(i[0])