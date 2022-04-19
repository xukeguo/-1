# coding=utf-8
#a = open("/Users/xuekguo/Documents/test.txt", "a+")
#print("http:\\\\www.baidu.com", file=a)
#a.close()   # 关闭文件
# 转义字符
print("55555\n44444")   
print("55555\b444")
print("55555\r44444")
print('55555\t44444')
print("hello\"")
print("http:\\\\www.baidu.com")
print(r"55555\n44444")
print(chr(0b10000001100111111))
print(ord('徐'))
# 导入
import keyword  # 导入模块

print(keyword.kwlist)   # 打印模块中的关键字
name = "科国"
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
print('值', name)
n = 10
print('类型', type(n))
print('八进制', 0o755)       # 八进制
print('二进制', 0b10101111)
print('十六进制', 0x789ad)
a = 1.1
a2 = 2.1
a3 = 2.2
print(a + a2)
print(a + a3)
from decimal import Decimal   # 导入模块

print(Decimal('1.1') + Decimal('2.2'))  # 对象操作
print('八进制', 0o755)     # 八进制
print('二进制', 0b10101111)            # 二进制
print('十六进制', 0x789ad)    # 十六进制
# 求随机数
import random  
    
 

print(0)
print(random.randint(0, 10))
b = 77.77
c = True
d = False
print(str(a), type(str(a)))
print(int(b), type(str(b)))
print(int(c), type(str(c)))
# 浮点数
print(float(a), type(a))
# 字符串
print(str(a), type(str(a)))
# 整数
print(int(b), type(int(b)))
# 布尔类型
a=2
b=bool(a)
print(b, type(b))
# 布尔值
print(True, type(True))
# 字符串
print(str(a), type(str(a)))
# 浮点数
print(float(a), type(float(a)))
# 字符串
print(str(a), type(str(a)))
# 整数
print(int(b), type(int(b)))
# 布尔值
print(int(c), type(int(c)))
# 转义字符
# 换行
print("55555\n44444")
# 删除
print("55555\b444")
# 回车
print("55555\r44444")
# 制表符
print('55555\t44444')
# 转义字符
print("hello\"")
# 转义字符
print("http:\\\\www.baidu.com")
# 转义字符
print(r"55555\n44444")
# 转义字符
print(chr(0b10000001100111111))
# 转义字符
print(ord('徐'))
# 转义字符
print(chr(0x789ad))
# 导入
import keyword
print(keyword.kwlist)
# name = "科国"
# print(name)
# print('标识', id(name))
# print('类型', type(name))
# print('值', name)
# print('值', name)
# n = 10
# print('类型', type(n))
# print('八进制', 0o755)
# print('二进制', 0b10101111)
# print('十六进制', 0x789ad)
# a = 1.1
# a2 = 2.1
# a3 = 2.2
# open("/Users/xuekguo/Documents/test.txt", "a+")
# 只读打开文件
# a = open("/Users/xuekguo/Documents/test.txt", "r")
# 读取文件
# print(a.read())
# 关闭文件
# a.close()
# 写入文件
# a = open("/Users/xuekguo/Documents/test.txt", "a+")
# 打开百度网页

#d = open("http:\\\\www.baidu.com", "a+")
#print("http:\\\\www.baidu.com", file=d)
#d.close()

# 数据类型-字符串
str1 = "hello world"  # 单个引号相当于单行文本
str2 = 'hello world'
str3 = """hello world"""  # 多行文本
str3 = """hello,
world"""  # 三个双引号相当于多行字符串
str4 = '''hello world'''
str5 = '''hello,
world'''
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
# 数据类型-整数
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)
# 数据类型-浮点数
a = 1.1
b = 2.2
c = 3.3
print(a)
print(b)
print(c)
# 数据类型-布尔值
a = True
b = False
print(a)
print(b)
# 注释编码转换
# coding:gbk
# coding:utf-8
# coding:utf-8
# 多行注释用三个单引号或者三个双引号，注意要用英文的引号
"""hello,
world"""

'''"""hello,
world"""'''
# 多行注释用三个单引号或者三个双引号，注意要用英文的引号
# 布尔值
a = True
b = False
#input 函数
a = input("请输入a的值：")
b = input("请输入b的值：")
print(int(a)+int(b))
#input 函数
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
print(a+b)
#input 函数
a =input("请输入a的值：")
a=int(a)
b =input("请输入b的值：")
b=int(b)
print(a**b)
#算术运算符
print(1+2)#加法
print(1-2)#减法
print(1*2)#乘法
print(1/2)#除法， 
print(1//2)#整除,公式被除数减去除数的商的整数部分
print(1%2)#取余
print(2**3)#乘方，2的3次方
#比较运算符
#等于
print(1==1)
#不等于
print(1!=1)                    # 不等于
#大于
print(1>1)         #False
print(2>1)         #True
#小于  
print(1<1)         #False
print(1<2)         #True         
#大于等于
print(1>=1)        #True
print(2>=1)        #True
#小于等于
print(1<=1)        #True
print(1<=2)        #True
#逻辑运算符
#与       
print(True and True)  #True
print(True and False) #False
print(False and False) #False                      
                         
#或
print(True or True)   #True
print(True or False)  #True
print(False or False) #False
#非    
print(not True)       #False
print(not False)      #True
#成员运算符
#in
print(1 in [1,2,3])   #True
print(6 in [1,2,3,4]) #False
#not in
print(1 not in [1,2,3])   #False 
print (8 not in [1,2,3])  #True
#身份运算符
#is
print(1 is 1)         #True
print(1 is not 1)     #False
#参数赋值运算符       #参数赋值运算符
a=20
a+=10# 相当于a=a+10
print(a)#30
a-=10# 相当于a=a-10
print(a)#20
a*=10# 相当于a=a*10
print(a)#200
a/=10# 相当于a=a/10
print(a)#20
a%=10# 相当于a=a%10
print(a)#0
a=111
a//=10# 相当于a=a//10
print(a)#11
a**=10# 相当于a=a**10   
print(a)#10000000000
a&=10# 相当于a=a&10   二进制与运算
print(a)#0
a|=10# 相当于a=a|10    二进制的或运算 
print(a)#10  
a=5
a^=10# 相当于a=a^10  二进制的异或运算
print(a)#10
a>>=10# 相当于a=a>>10
print(a)#0
a<<=10# 相当于a=a<<10
print(a)#0

#指向变量的指针
a = 10
b = a
print(b)            # 10

#**
print(2**3)#8
#指数运算符
#a^10什么意思？  
#a**10什么意思？  a的10次方
a=3
print(a^10)   
a=6
a=a|10  
print(a) 
#解包赋值
a,b,c=1,2,3
print(a,b,c,) #1 2 3   解包赋值         
#解包赋值
a,b,c=1,2,3
c,b,a=a,b,c   #交换a,b,c的值    
print(a,b,c,) #3 2 1   解包赋值
  #定义布尔类型函数  bool
#位运算符  &  |  ^  ~  <<  >>
# 位与运算符&：两个二进制数的对应位都为1，结果位就为1，否则为0。  a&b
# 位或运算符|：两个二进制数的对应位中有一个为1，结果位就为1，否则为0。  a|b
# 位异或运算符^：两个二进制数的对应位不同时，结果位就为1，否则为0。  a^b
# 位反转运算符~：对数据的每一位取反，即把1变为0，0变为1。  ~a
# 位左移运算符<<：运算数的各二进位全部左移若干位，由右边开始，其余位补0。  a<<2
# 位右移运算符>>：运算数的各二进位全部右移若干位，由左边开始，其余位补0。  a>>2
# 位移运算符  <<  >>  &  |  ^  ~  *  /  %  **  //  +=  -=  *=  /=  %=  
# **=  //=  &=  |=  ^=  <<=  >>=
#               运算符的优先级
#            ** 优先级最高，指数运算符   
#            *  /  %  优先级第二
#            +  -  优先级第三
#            <<  >>  优先级第四 
#            &  |  ^  优先级第五
#            ~  优先级第六
#            =  优先级第七
#            <  >  <=  >=  优先级第八
#            !=  ==  优先级第九
#            and  or  not  优先级第十
#            (  )  [  ]  {  }  优先级第十一
#            ,  :  ;  .  ?  =  优先级第十二
#            is  is not  in  not in  优先级第十三
#            not  and  or  优先级第十四
#            +=  -=  *=  /=  %=  **=  <<=  >>=  &=  |=  ^=  优先级第十六
#            and  or  not  优先级第十七
#以下对象的布尔值为False：
#空字符串，None，0，0.0，空列表，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象
print (bool(''))
print (bool(None))
print (bool(0))  
print (bool(0.0))  
print (bool([]))#空列表
print (bool(())) #空元组
print (bool({})) #空字典
print (bool(set()))  #空集合
print (bool('')) #空字符串
print (bool(open('1.py')))  #空文件
print (bool(list())) #空列表
print (bool(tuple())) #空元组
print (bool(dict())) #空字典
print (bool('')) #空字符串
#以下对象的布尔值为True：
#非空字符串，非None，非0，非0.0，非空列表，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空闭包，非空类型，非空模块，非空类型，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空闭包，非空类型，非空模块，非空类型，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空
#字典的定义
dict1={'name':'张三','age':18,}#字典的定义
dict2=dict(name='张三',age=18,)
dict()#字典的定义
print (dict2) #{'name': '张三', 'age': 18}
dict1['name']='李四' #修改
print (dict1) #{'name': '李四', 'age': 18}
#字典的删除
del dict1['name']
print (dict1) #{'age': 18}
#字典的遍历
dict1={'name':'张三','age':18,}
for key in dict1:#遍历字典的键
    print (key) #name age
for k in dict1:
    print (dict1[k]) #张三 18
for key in dict1:
    print (key,dict1[key]) #name 张三 age 18
#字典的排序
dict1={'name':'张三','age':18,}
print (sorted(dict1)) #['age', 'name']
print (sorted(dict1.items())) #[('age', 18), ('name', '张三')]
print (sorted(dict1.values())) #['张三', 18]
#字典的拷贝
dict1={'name':'张三','age':18,}
dict2=dict1.copy()
print (dict2) #{'age': 18, 'name': '张三'}
#字典的查找
dict1={'name':'张三','age':18,}
print (dict1.get('name')) #张三 GET方法（）字符要‘’字符的查找匹配都要用‘’字符 GEt方法只找键
name=dict1.get('nam')
a=(name)
b =0.1114
print (type(b )) #<class 'float'>
print (a) #张三
print (dict1.get('age')) #18
#字典的添加
#字典的索引
#字典的切片
#字典的计数
dict1={'name':'张三','age':18,}
print (dict1.items()) #dict_items([('age', 18), ('name', '张三')])
a=dict1.items()
print (type(a)) #dict_items([('age', 18), ('name', '张三')])
print (dict1.keys()) #dict_keys(['age', 'name'])
print (dict1.values()) #dict_values([18, '张三'])
#字典的排序 
#字典的拷贝  
#字典的遍历 
#字典的查找             


dict1={'name':'张三','age':18,}#字典的添加  
dict1[' 地址 ']=' 湖南 ' #字典的添加  
print (dict1) # {'age': 18, 'name': '张三', ' 地址 ': ' 湖南 '}
#组合字典示例
  
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,} 
#字典的更新 dict1.update(dict2)
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,}
dict1.update(dict2)
print (dict2) #{'age': 19, 'name': '李四'}
print (dict1) #{'age': 19, 'name': '李四'}
#字典的更新 dict1.update(dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15,dict16,dict17,dict18,dict19,dict20,dict21,dict22,dict23)
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,}
dict3={'name':'王五','age':20,}
mydict=dict1.copy()
mydict.update(dict2)
print (mydict) #{'age': 20, 'name': '王五'}
a=print (dict1) #{'age': 18, 'name': '张三'}
print(type(a))

#字典的更新 dict1.update(dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15,dict16,dict17,dict18,dict19,dict20,dict21,dict22,dict23)
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,}
dict3={'name':'王五','age':20,}
mydict=dict1.copy()
mydict.update(dict2)
print (mydict) #{'age': 20, 'name': '王五'}
#字典的添加

#判断字典是否为空
dict1={'name':'张三','age':18,}
if dict1:
    print ('字典不为空')
else:
    print ('字典为空')  
#字典的键值对,python中的字典是无序的,所以字典的键值对是无序的,视图排序
dict1={'name':'张三','age':18,}
print (dict1.items()) #dict_items([('age', 18), ('name', '张三')])  
print (dict1.keys()) #dict_keys(['age', 'name'])    
print (dict1.values()) #dict_values([18, '张三'])
#判断查找dict1中是否包含key
dict1={'name':'张三','age':18,} 
if 'name' in dict1.keys():
    print ('字典中包含name',dict1['name'])  
else:
    print ('字典中不包含name')
#判断查找dict1中是否包含value

dict1={'name':'张三','age':18,}
if '张三' in dict1.values():
    print ('字典中包含张三的索引',dict1['name'])
else:
    print ('字典中不包含张三')
#判断查找dict1中是否包含key和value
dict1={'name':'张三','age':18,}
if ('name','张三') in dict1.items():
    print ('字典中包含name和张三')
else:
    print ('字典中不包含name和张三')
#判断奇数偶数
dict1={'name':'张三','age':18,}
if dict1['age']%2==0:
    print ('字典中的age是偶数')
else:
    print ('字典中的age是奇数')
    #判断key是否匹配
dict1={'name':'张三','age':18,}
if dict1.keys()==('name','age'):
    print ('字典中的key是name和age')
else:
    print ('字典中的key不是name和age')
#判断value是否匹配
dict1={'name':'张三','age':18,}
if dict1.values()==('张三',18):
    print (dict1.values()) #('张三', 18)
dict1={'name':'张三','age':18,}
if dict1['name']=='张三':
        print ('字典中的value是name和张三')
else:
        print ('字典中的value不是name和张三')
#字典的排序
dict1={'name':'张三','age':18,}
print (sorted(dict1)) #['age', 'name']
print (sorted(dict1.items())) #[('age', 18), ('name', '张三')]

 #提取字典中的key
dict1={'name':'张三','age':18,}
score= (dict1.keys()) #dict_keys(['age', 'name'])
print (score) #('age', 'name')
#提取字典中的一个key用作变量？
dict1={'name':'张三','age':18,}
#提取字典中的value
dict1={'name':'张三','age':18,}
score= (dict1.values()) #dict_values([18, '张三'])         #提取字典中的一个value用作变量？



#创建学生信息字典
dict1={}
input_student = input('请输入学生姓名：')
dict1['name']=input_student
input_age = input('请输入学生年龄：')
dict1['age']=input_age
input_score = input('请输入学生成绩：')
dict1['score']=input_score
print (dict1)
#字典视图排序
dict1={'name':'张三','age':18,}
print (sorted(dict1.items())) #[('age', 18), ('name', '张三')]
print (sorted(dict1.keys())) #['age', 'name']
print (sorted(dict1.values())) #[18, '张三']
#字典的生成式
list1=[ '张三', '李四', '王五', '赵六', '田七', '钱八', '孙九', '周十']
list2=[18,19,20,21,22,23,24,25]
print (dict(zip(list1,list2))) #{'张三': 18, '李四': 19, '王五': 20, '赵六': 21, '田七': 22, '钱八': 23, '孙九': 24, '周十': 25}
print(type(list1)) #<class 'list'>
list3=[90,80,70,60,50,40,30,20]
dict1={ x:[y,z] for x,y,z in zip(list1,list2,list3)}
dict2={ x:y for x,y in zip(list1,list2)}
print(type(dict1)) #<class 'dict'>
print (dict1)
print (dict2)
#元组的生成式
t=('iii','jjj','fff')
print (type(t)) #<class 'tuple'>
t1=tuple(t)
print (t1)
#generator 什么类型  
#generator是一种返回值不是一个数值的函数，而是一个返回值是一个迭代器的函数。
#generator函数是一个状态有状态的函数，可以记住上次执行的状态，并且在下次执行时，从上次执行的状态开始执行。
#集合的生成式
set1={x for x in range(10)}
print (type(set1)) #<class 'set'>
print (set1)
#集合的生成
set1={2,3,4,5,6,7,8,9,10}
set2=set(range(10)) #用set函数生成集合
set3={x for x in range(10) if x%2==0}
set4={x for x in range(10) if x%2!=0}#集合的生成式或者推导式
print (type(set2)) #<class 'set'>
#集合的运算符号  并集& 
#集合的交集
print (set1 & set2) #{2, 3, 4, 5, 6, 7, 8, 9}
#集合的并集
print (set1 | set2) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#集合的差集
print (set1 - set2) #{0, 1}
print (set2 - set1) #{10}
#集合的对称差集
print (set1 ^ set2) #{0, 1, 10}
#集合的子集
print (set1 <= set2) #false
#集合的超集
print (set1 >= set2) #false
#集合的子集
print (set1 < set2) #False
#集合的超集
print (set1 > set2) #False
#集合的对称差集
print (set1 != set2) #True
#集合的对称差集
print (set1 == set2) #False
#集合的移除
set1.remove(2)#
print (set1) #{3, 4, 5, 6, 7, 8, 9, 10}
#集合的添加
set1.add(11)
set1.update([12,13,14])# 添加多个元素
print (set1) #{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
#集合的
set1.discard(11)#把11从集合中移除
print (set1) #{3, 4, 5, 6, 7, 8, 9, 10}
set1.pop()#随机移除一个元素
set1.clear()#清空集合
set1.difference_update([1,2,3])#把集合中的元素从另一个集合中移除
set1.isdisjoint(set2)#判断两个集合是否有交集
set1.issubset(set2)#判断一个集合是否是另一个集合的子集
set1.issuperset(set2)#判断一个集合是否是另一个集合的超集
set1.union(set2)#求两个集合的并集
set1.intersection(set2)#求两个集合的交集
set1.symmetric_difference(set2)#求两个集合的对称差集
set1.difference(set2)#求两个集合的差集
set1.copy()#拷贝一个集合
set1.update([1,2,3])#添加多个元素
print (set1.issubset( set2)  ) #True
set1.remove(1)#移除一个元素
set1.discard(1)#移除一个元素，如果不存在，不会报错  
set1.pop()#随机移除一个元素
set1.clear()#清空集合
#字符串的生成式
str1='abc|defg'# 字符串的生成式
str2 = ''.join(['a','b','c'])#连接字符串
print (str2)
print (str1)
#字符串的添加
str1='abc'
str1+='def'
print (str1)
#字符串的删除    方法为切片
str1='abcdef'
str1=str1[2:-3]#删除第三个到倒数第三个字符
print (str1)
   
str1='abcdef王王g'
str1 
print (str1)
str1.index( c) #查找字符串中第一次出现的字符c的索引
str1.count(c) #查找字符串中出现的字符c的个数
str1.find(c) #查找字符串中第一次出现的字符c的索引
str1.rfind(c) #查找字符串中最后一次出现的字符c的索引
str1.startswith(c) #判断字符串是否以c开头   false
str1.endswith(c) #判断字符串是否以c结尾   false
str1.isalnum() #判断字符串是否由字母和数字组成   false
str1.isalpha() #判断字符串是否由字母组成   true
str1.upper() #将字符串中的小写字母转换成大写字母
str1.lower() #将字符串中的大写字母转换成小写字母
str1.capitalize() #将字符串的第一个字母转换成大写字母
str1.title() #将字符串中每个单词的第一个字母转换成大写字母
str1.swapcase() #将字符串中的大写字母转换成小写字母，小写字母转换成大写字母
str1.strip() #删除字符串首尾的空格
str1.lstrip() #删除字符串左边的空格
str1.rstrip() #删除字符串右边的空格
str1.replace(old,new) #将字符串中的old字符串替换成new字符串
str1.split(sep='|',maxsplit=1) #将字符串按照c字符串进行分割，返回一个列表
str1.join(str2) #将字符串str2中的每个元素替换成str1
print (str1.split(sep='|',maxsplit=1)) #['abc', 'defg']
print (str1.join(str2)) #abc|defg
print(str2)#abc|defg
str1.join(list) #将list中的每个元素替换成str1
str1.encode(encoding='utf-8',errors='strict') #将字符串转换成字节码
str1.decode(encoding='utf-8',errors='strict') #将字节码转换成字符串
str1.format(a,b,c) #格式化字符串
str1.zfill(width) #将字符串填充为指定长度，不足的在左边填充0
str1.center(width) #将字符串填充为指定长度，不足的在中间填充空格
str1.ljust(width) #将字符串填充为指定长度，不足的在左边填充空格
str1.rjust(width) #将字符串填充为指定长度，不足的在右边填充空格
str1.isdigit() #判断字符串是否只由数字组成
str1.isalpha() #判断字符串是否只由字母组成
str1.isalnum() #判断字符串是否只由字母和数字组成
str1.isupper() #判断字符串是否只由大写字母组成
str1.islower() #判断字符串是否只由小写字母组成
str1.istitle() #判断字符串是否只由标题字母组成
str1.isspace() #判断字符串是否只由空格组成
str1.isnumeric() #判断字符串是否只由数字组成
str1.isidentifier() #判断字符串是否是合法的标识符
str1.expandtabs(tabsize=8) #将字符串中的tab符号转换成空格，tabsize指定tab的长度
str1.lstrip() #删除字符串左边的空格
str1.rstrip() #删除字符串右边的空格
str1.strip() #删除字符串首尾的空格
str1.lower() #将字符串中的大写字母转换成小写字母
#将字符串中的小写字母转换成大写字母
str1.upper()
#ord()函数获取字符的整数表示与chr()函数相反
print(ord('a')) #97
print(ord('A')) #65
print(ord('中')) #20013
print(chr(97)) #a
print(chr(65)) #A
print(chr(20013)) #中
#len()函数获取字符串的长度
print(len('abc')) #3
print(len('中文')) #2
#str()函数将其他类型转换成字符串
print(str(123)) #123
print(str(123.456)) #123.456
print(str(True)) #True  
print(str(None)) #None
#repr()函数将其他类型转换成字符串   
print(repr(123)) #123
print(repr(123.456)) #123.456   
print(repr(True)) #True
print(repr(None)) #None
#eval()函数将字符串转换成表达式，并返回表达式的值
print(eval('1+2')) #3
print(eval('1+2+3')) #6
print(eval('1+2+3+4')) #10
#exec()函数将字符串转换成表达式，并执行表达式
exec('print("hello")') #hello
#格式化字符串 第一种用占位符 % %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数 %o 八进制整数 %e 指数 %.2f 保留两位小数  
print('%s' % 'abc') #abc
print('%d' % 123) #123
print('%f' % 123.456) #123.456
print('%x' % 123) #7b   
print('%o' % 123) #173
print('%s' % '中文') #中文
print('%s' % '中文'.encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'
print('%s' % '中文'.encode('utf-8').decode('utf-8')) #中文
print('%s' % '中文'.encode('utf-8').decode('utf-8').encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'
print('%s' % '中文'.encode('utf-8').decode('utf-8').encode('utf-8').decode('utf-8')) #中文
print('%s' % '中文'.encode('utf-8').decode('utf-8').encode('utf-8').decode('utf-8').encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'   
#字符串格的编码  解码
s='存在的不一定合理'
s_byte1=s.encode('utf-8')#编码
print(s_byte1) #b'\xe5\xad\x98\xe5\x9c\x9f\xe4\xb8\x8d\xe4\xb8\x80\xe5\x90\xab\xe5\x90\x9b\xe7\x90\x86'
print(s_byte1.decode('utf-8')) #  存在的不一定合理，解码
s_byte2=s.encode('gbk')#编码
print(s_byte2) #b'\xad\x98\xad\x9c\xad\x9f\xad\x8d\xad\x8d\xad\x9b\xad\x90\xad\x9b\xad\x86'
print(s_byte2.decode(encoding='gbk')) #存在的不一定合理,解码
s_byte3=s.encode('gbk').decode('gbk')#编码

#字符串的比较
print('abc'<'abd') #True
print('abc'<'abd'<'abf') #True
print('abc'<'abd'<'abf'<'abg') #False
print('abc'<'abd'<'abf'<'abg'<'abh') #False
print('abc'<'abd'<'abf'<'abg'<'abh'<'abj') #True
#字符串的拼接
print('abc'+'def') #abcdef
print('abc'+'def'+'ghi') #abcdefghi
print('abc'+'def'+'ghi'+'jkl') #abcdefghijkl
print('abc'+'def'+'ghi'+'jkl'+'mno') #abcdefghijklmno
print('abc'+'def'+'ghi'+'jkl'+'mno'+'pqr') #abcdefghijklmnopqr
print('abc'+'def'+'ghi'+'jkl'+'mno'+'pqr'+'stu') #abcdefghijklmnopqrstu
print('abc'+'def'+'ghi'+'jkl'+'mno'+'pqr'+'stu'+'vwx') #abcdefghijklmnopqrstuvwx
print('abc'+'def'+'ghi'+'jkl'+'mno'+'pqr'+'stu'+'vwx'+'yz') #abcdefghijklmnopqrstuvwxyz
#字符串的切片
print('abcdefghijklmnopqrstuvwxyz'[0:3]) #abc
#


name = '张三'
age = 18
gender='男'
print('我叫%s，真的叫%s,今年%d岁,性别%s' % (name,name, age,gender)) #我叫张三，今年18岁 
print ('我叫{0}，真的叫{0},今年{1}岁,性别{2}' .format (name, age,gender))# 第二种用.format 
print (f'我叫{name}，真的叫{name},今年{age}岁,性别{gender}') # 第三用种f
#绝
     
 
     

 
     


     







 







