#!/bin/bash/python
#coding=utf-8
from __future__ import division
import random
import time
print "********************"
while True:
    flag=raw_input("按(C)键出题或继续练习，或按任意其他字母键退出 : ")
    flag=flag.lower()
    if flag=="c":
        start = time.clock()
        indicator=random.randint(5,20)
        example_list=[]
        example_str=""
        for i in xrange(indicator):
            num=random.randint(65,122)
            while num >= 91 and num <= 96:
               num=random.randint(65,122)
            example_list.append(chr(num))
        example_str="".join(example_list)
        print "请输入旁边",indicator,"个字母：",example_str
        user_input=raw_input("：")
        if len(user_input)>indicator:
            print "输入的字母超过规定的字母数"
        else:
            Correct_Num=0
            myrange=min(len(example_str),len(user_input))
            for j in xrange(myrange):
                if user_input[j]==example_str[j]:
                    Correct_Num+=1
            if 75<=((Correct_Num*1.0)/indicator*100)<85:
                print "良好，正确率%.2f%%"%((Correct_Num*1.0)/indicator*100)
                end = time.clock()
                print('使用时间: %s 秒'%int(end-start))
            elif ((Correct_Num*1.0)/indicator*100)<60:
                print "不及格，正确率%.2f%%"%((Correct_Num*1.0)/indicator*100)
                end = time.clock()
                print('使用时间: %s 秒'%int(end-start))
            elif ((Correct_Num*1.0)/indicator*100)>=85:
                print "优秀，正确率%.2f%%"%((Correct_Num*1.0)/indicator*100)
                end = time.clock()
                print('使用时间: %s 秒'%int(end-start))
            elif 60<=((Correct_Num*1.0)/indicator*100)<=75:
                print "及格，正确率%.2f%%"%((Correct_Num*1.0)/indicator*100)
                end = time.clock()
                print('使用时间: %s 秒'%int(end-start))

    else:
        break
