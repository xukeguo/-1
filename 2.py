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
print(float(a), type(float(a)))
# 字符串
print(str(a), type(str(a)))
# 整数
print(int(b), type(int(b)))
# 布尔值
print(int(c), type(int(c)))
# 布尔值
print(int(d), type(int(d)))
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
a&=10# 相当于a=a&10
print(a)#0
a|=10# 相当于a=a|10     
print(a)#10
a^=10# 相当于a=a^10
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
dict1={'name':'张三','age':18,}
print (dict1) #{'name': '张三', 'age': 18}
dict1['name']='李四' #修改
print (dict1) #{'name': '李四', 'age': 18}
#字典的删除
del dict1['name']
print (dict1) #{'age': 18}
#字典的遍历
dict1={'name':'张三','age':18,}
for key in dict1:
    print (key) #name age
for key in dict1:
    print (dict1[key]) #张三 18
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
#字典的添加  
dict1={'name':'张三','age':18,}
dict1[' 地址 ']=' 湖南 ' #字典的添加  
print (dict1) # {'age': 18, 'name': '张三', ' 地址 ': ' 湖南 '}
#组合字典示例
  
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,} 
#字典的更新 dict1.update(dict2)
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,}
dic1.update(dic2)
print (dic2) #{'age': 19, 'name': '李四'}
#字典的更新 dict1.update(dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15,dict16,dict17,dict18,dict19,dict20,dict21,dict22,dict23)
dict1={'name':'张三','age':18,}
dict2={'name':'李四','age':19,}
dict3={'name':'王五','age':20,}
mydict=dict1.copy()
mydict.update(dict2)
print (mydict) #{'age': 20, 'name': '王五'}
#字典的更新 dict1.update(dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15,dict16,dict17,dict18,dict19,dict20,dict21,dict22,dict23)


#判断字典是否为空
dict1={'name':'张三','age':18,}
if dict1:
    print ('字典不为空')
else:
    print ('字典为空')  
#字典的键值对
dict1={'name':'张三','age':18,}
print (dict1.items()) #dict_items([('age', 18), ('name', '张三')])  
print (dict1.keys()) #dict_keys(['age', 'name'])    
print (dict1.values()) #dict_values([18, '张三'])
#判断dict1中是否包含key
dict1={'name':'张三','age':18,} 
if 'name' in dict1:
    print ('字典中包含name')
else:
    print ('字典中不包含name')
#判断dict1中是否包含value
dict1={'name':'张三','age':18,}
if '张三' in dict1.values():
    print ('字典中包含张三')
else:
    print ('字典中不包含张三')
#判断dict1中是否包含key和value
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
 







