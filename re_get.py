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
answer = [0]*555
re_get = []

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
        qst_comment = qst_info[1].strip().split('\n')  #问题的标记信息 发布时间和回答数量
        #print(len(qst_comment[0]))
        ans_num = int(qst_comment[1][5:])
        #print("回答数量：%d  抓取数量：%d" % (ans_num,len(ls)-1))
        #print("抓取数量：%d"%(len(ls)-1))
        return ans_num, len(ls)-1
        

def main():
    recnt=0
    with open("need_re_get.txt", 'w', encoding='utf-8') as f1:
        for i in range(0,555):
            if i !=388:
                ans_num,real_num = cal(i)
                answer[i] = real_num
                if ans_num != real_num:
                    print("(%d %d)"%(ans_num,real_num))
                    print("需要重新抓取的编号：%d"%i)
                    f1.write("编号："+str(i)+" 已抓取："+str(real_num)+" 总数量："+str(ans_num)+"\n")
                    recnt = recnt + 1
                    re_get.append(i)
        print(recnt)
        f1.write("还需抓取的问题个数为："+str(recnt))
   # for i in range(0,555):
   #print(answer[i])
    print(len(re_get)) 
    print(re_get)
   
if __name__ == '__main__':
    main()