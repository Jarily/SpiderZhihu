# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:31:35 2018

@author: Jarily
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:31:40 2018

@author: jarily
"""

kw = ['爆炸','救援','撤离','调查','追责','居民','瑞海','媒体','市政府','消防','公安','安监局','环保局','环境','污染','空气','废水','化学品','氰','环评']

def get_question_date(index):
    fname = 'question_clean/question' + str(index) + '.txt'
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
        #print(qst_info[1])
        qst_comment = qst_info[1].strip().split('\n')  #问题的标记信息 发布时间和回答数量
        return qst_comment[0][5:]




def get_answer_date(index):
    fname = 'question_clean/question' + str(index) + '.txt'
    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()
        #print(data)
        ls = data.split("###\n")
                        
        res = []
        
        #print(ls)
        if len(ls) == 1: #没有回答
            return res 
        
        for i in range(1,len(ls)):
            #print(i)
            ans_info = ls[i].strip().split("---\n")
            ans_comment = ans_info[1].strip().split('\n')
            res.append(ans_comment[1][5:])
            #print(ans_comment[1][5:])
        return res        

def get_answer_usr(index):
    fname = 'question_clean/question' + str(index) + '.txt'
    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()
        #print(data)
        ls = data.split("###\n")
        
        res = []
        
        #print(ls)
        if len(ls) == 1: #没有回答
            return res 
        
        for i in range(1,len(ls)):
            #print(i)
            ans_info = ls[i].strip().split("---\n")
            ans_comment = ans_info[1].strip().split('\n')
            res.append(ans_comment[2][5:])
            print(ans_comment[2][5:])
        return res    

def get_answer_data(index,k):
    fname = 'question_clean/question' + str(index) + '.txt'
    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()
        #print(data)
        ls = data.split("###\n")
        
        kk = 0
        
        if len(ls) == 1: #没有回答
            return kk         
        
        for i in range(1,len(ls)):
            #print(i)
            ans_info = ls[i].strip().split("---\n")
            kk= kk + ans_info[0].count(kw[k])
            #print(ans_info[0])
        return kk

qst_usrs = set()

def count_qst_usr():
    with open('data_res/question_usr.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        niming = 0
        res = []
        for line in lines:
            if line.strip() == '匿名用户':
                niming = niming +1
            else:
                if line.strip() in qst_usrs:
                    pass
                else:
                    res.append(line.strip())
                    qst_usrs.add(line.strip())
        return niming + len(res), len(lines)

def count_ans_usr():
    with open('data_res/answer_usr.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        niming = 0
        res = []
        for line in lines:
            if line.strip() == '匿名用户':
                niming = niming +1
            else:
                if line.strip() in qst_usrs:
                    pass
                else:
                    res.append(line.strip())
                    qst_usrs.add(line.strip())
        return niming + len(res), len(lines)

songjia = {}
jiabao = {}

node0 = ['2015-08-12','2015-08-13','2015-08-14','2015-08-15','2015-08-16','2015-08-17','2015-08-18']
 
node1 = ['2015-08-12,2015-08-17','2015-08-19,2015-08-25','2015-08-26,2015-09-01','2015-09-02,2015-09-08','2015-09-09,2015-09-30','2015-10-01,2015-10-31','2015-11-01,2015-11-30','2015-12-01,2015-12-31','2016-01-01,2016-12-31','2017-01-01,2017-12-31','2018-01-01,now']
#                   0                       1                        2                       3                       4                       5                       6                       7                       8                      9                       10                   
          


def count_qst_date():
    
    for k in node0:
        songjia[k] = 0
    for k in node1:
        songjia[k] = 0
    
    with open('data_res/question_time.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines() 
        #print(lines)
        for line in lines:
            line = line.strip()
            year = int(line[0:4])
            mon = int(line[5:7])
            day = int(line[8:])
            
            if line in node0:
                songjia[line]= songjia[line] + 1
            if year == 2015 and mon == 8 and day >= 12 and day <= 17:
                songjia[node1[0]] = songjia[node1[0]] + 1
            elif year == 2015 and mon == 8 and day >= 19 and day <= 25:
                songjia[node1[1]] = songjia[node1[1]] + 1
            elif year == 2015 and (mon == 8 and day >= 26) or (mon == 9 and day <= 1):
                songjia[node1[2]] = songjia[node1[2]] + 1               
            elif year == 2015 and mon == 9 and day >= 2 and day <= 8:
                songjia[node1[3]] = songjia[node1[3]] + 1
            elif year == 2015 and mon == 9 and day >= 9 and day <= 30:
                songjia[node1[4]] = songjia[node1[4]] + 1
            elif year == 2015 and mon == 10 and day >= 1 and day <= 31:
                songjia[node1[5]] = songjia[node1[5]] + 1
            elif year == 2015 and mon == 11 and day >= 1 and day <= 30:
                songjia[node1[6]] = songjia[node1[6]] + 1
            elif year == 2015 and mon == 12 and day >= 1 and day <= 31:
                songjia[node1[7]] = songjia[node1[7]] + 1
            elif year == 2016:
                songjia[node1[8]] = songjia[node1[8]] + 1
            elif year == 2017:
                songjia[node1[9]] = songjia[node1[9]] + 1
            elif year == 2018:
                songjia[node1[10]] = songjia[node1[10]] + 1
 
def count_ans_date():
    
    for k in node0:
        jiabao[k] = 0
    for k in node1:
        jiabao[k] = 0
    
    with open('data_res/answer_time.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines() 
        #print(lines)
        for line in lines:
            line = line.strip()
            year = int(line[0:4])
            mon = int(line[5:7])
            day = int(line[8:])
            
            if line in node0:
                jiabao[line]= jiabao[line] + 1
            if year == 2015 and mon == 8 and day >= 12 and day <= 17:
                jiabao[node1[0]] = jiabao[node1[0]] + 1
            elif year == 2015 and mon == 8 and day >= 19 and day <= 25:
                jiabao[node1[1]] = jiabao[node1[1]] + 1
            elif year == 2015 and (mon == 8 and day >= 26) or (mon == 9 and day <= 1):
                jiabao[node1[2]] = jiabao[node1[2]] + 1               
            elif year == 2015 and mon == 9 and day >= 2 and day <= 8:
                jiabao[node1[3]] = jiabao[node1[3]] + 1
            elif year == 2015 and mon == 9 and day >= 9 and day <= 30:
                jiabao[node1[4]] = jiabao[node1[4]] + 1
            elif year == 2015 and mon == 10 and day >= 1 and day <= 31:
                jiabao[node1[5]] = jiabao[node1[5]] + 1
            elif year == 2015 and mon == 11 and day >= 1 and day <= 30:
                jiabao[node1[6]] = jiabao[node1[6]] + 1
            elif year == 2015 and mon == 12 and day >= 1 and day <= 31:
                jiabao[node1[7]] = jiabao[node1[7]] + 1
            elif year == 2016:
                jiabao[node1[8]] = jiabao[node1[8]] + 1
            elif year == 2017:
                jiabao[node1[9]] = jiabao[node1[9]] + 1
            elif year == 2018:
                jiabao[node1[10]] = jiabao[node1[10]] + 1    
    
    
    
def main():
    n = 519
    '''
    # 获取问题发布时间
    with open("data_res/question_time.txt", 'w', encoding='utf-8') as f1:
        for i in range(0,n):
            date = get_question_date(i)
            f1.write(date+'\n')
                
    # 获取问题回答时间
    with open("data_res/answer_time.txt", 'w', encoding='utf-8') as f1:
        for i in range(0,n):
            print("处理第%d组数据"%i)
            date = get_answer_date(i)
            if len(date)>0:
                for j in range(0,len(date)):
                    if '2015' not in date[j] and '2016' not in date[j] and '2017' not in date[j] and '2018' not in date[j]:
                        print("出现了异常,  第%d组数据的第%d条回答"%(i,j+1))
                        print(date[j])
                        return
                    f1.write(date[j]+'\n')
    
    # 获取回答问题的用户名             
    with open("data_res/answer_usr.txt", 'w', encoding='utf-8') as f1:
        for i in range(0,n):
            date = get_answer_usr(i)
            if len(date)>0:
                for j in range(0,len(date)):
                    f1.write(date[j]+'\n')
    
    with open("data_res/kw_num.txt", 'w', encoding='utf-8') as f1:
        f1.write("关键词  出现频次"+'\n'+'----------------\n')
        for k in range(0,len(kw)): #len(kw)):
            print("处理第%d个关键字：%s"%(k, kw[k]))
            kcnt = 0
            for i in range(0, n):
                kcnt += get_answer_data(i,k)
                #print("处理第%d组数据"%i)
            print(kcnt)
            kkw = kw[k]
            for j in range(len(kw[k]),10):
                kkw = kkw + ' '
            f1.write(kkw+str(kcnt)+'\n')
    
    with open("data_res/usr_sum.txt", 'w', encoding='utf-8') as f1:
        qst_usr_sum, qst_sum = count_qst_usr()
        ans_usr_sum, ans_sum = count_ans_usr()
        print("提问账户数量为：%d，回答账户数量为：%d"%(qst_usr_sum,ans_usr_sum))
        f1.write("总问题数量为："+str(qst_sum)+"，总回答数量为："+str(ans_sum)+'\n')
        f1.write("提问账户数量为："+str(qst_usr_sum)+"，回答账户数量为："+str(ans_usr_sum))
    
    with open("data_res/temporal_distribution.txt", 'w', encoding='utf-8') as f1:
        count_qst_date()
        count_ans_date()
        f1.write("问题发布时间的分布："+'\n'+'-------------------------------------\n')

        for k in songjia.keys():
            print(k)
            tmp = k
            for j in range(len(k),30):
                tmp = tmp + ' '
            print(songjia[k])
            f1.write(tmp+str(songjia[k])+'\n')

        f1.write("\n\n\n回答发布时间的分布："+'\n'+'-------------------------------------\n')

        for k in jiabao.keys():
            print(k)
            tmp = k
            for j in range(len(k),30):
                tmp = tmp + ' '
            print(jiabao[k])
            f1.write(tmp+str(jiabao[k])+'\n')
        print(songjia)
        print(jiabao)
    '''
if __name__ == '__main__':
    main()