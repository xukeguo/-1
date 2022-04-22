#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   demo1.py
#@Time    :   2022/04/19 23:25:21
#@Author  :   flow-laic 
#@Email   :

from email import header


header_charset = 'ISO-8859-1'
from asyncore import file_dispatcher
from base64 import encode
from urllib import request

#encode('utf-8')
a=100
sdf=200


def f():
    a=200
    print(a)
    if __name__=='__main__':
    
      print('b',sdf)
    return a


f()
#系统库
import sys
print(sys.path)
#自定义库
import urllib#
print(urllib.request.urlopen('http://www.baidu.com').read())
#time
import time
print(time.localtime(time.time()))
import sched#一定间隔执行
import time
def job():
    print('I am job')
    print(time.localtime(time.time()))
    s.enter(10,1,job)
s=sched.scheduler(time.time,time.sleep)
s.enter(3,1,job)
s.run()

import sched#!一定间隔执行
import time
if __name__=='__main__':# 只有在当前模块被直接执行时才会执行调用
 def job2():
    print('I am job2') 
    s.enter(3,1,job2)
s=sched.scheduler(time.time,time.sleep)
s.enter(3,1,job2)
s.run()
#pip intall requests 
from urllib import request
print(request.get('http://www.baidu.com'))
#读取文件
f=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','r')
print(f.readline())
f.close()
#读取文件2
with open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','r') as f:
    print(f.read())




#写入文件
b=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','a+')
b.write('good')
print('good,hello world',file=b)#任何语句都可赋值给=，也可以print
b.close()
