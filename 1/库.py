list_mame=['Waiwu','Lisi','Wangwu','Zhaoliu','Zhangsan']
for i in range(0,len(list_mame)):
    if 'hao' in list_mame[i]:
        print(list_mame[i],i)
for x in list_mame:    
 if 'Waiw' in x:
  print (x.index)
for i in range(0,len(list_mame)):
    print('姓名：',list_mame[i],'年龄：',list_age[i],'成绩：',list_score[i])
# for i in range(len(list_mame)):
list_age=[18,19,20,21,22]
list_score=[90,80,70,60,50]
a=sum(list_age)#列表求和
b=max(list_score)#获取列表中的最大值    
def max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(max(list_score))
c=min(list_age)#获取列表中的最小值
def my_min(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min
d=(list_age)
#获取列表的平均值
def my_average(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
print(b)

list_mame=['Waiwu','Lisi','Wangwu','Zhaoliu','Zhangsan']
list1=list(list_age+list_score+[100])
print(list1)
list2=list(zip(list_score,list_age))
print(list1)
list_mame=['Waiwu','Lisi','Wangwu','Zhaoliu','Zhangsan']
dict1={x:[y,z] for x,y,z in zip(list_mame,list_age,list_score)}
print(dict1)
dict2={x:y for x,y in zip(list_mame,list_age)}
dict6=dict(dict2)
#dict6=dict(dict2,**dict1)#合并字典?
print(dict6)
dict5={'Wangwu1':[20,90]}
dict7=dict(dict1,**{'Waiwu1':110})#合并字典修改
print(dict7)
dict7.update({'Warning1':100})#字典追加与列表的.append()类似
print(dict7)
dict3=dict(zip(list_mame,list_age))
print(dict3)
print(dict1['Waiwu'][0])
list1=dict1['Waiwu']
print(dict1)
a=0
for i in range(len(list_mame)):
    for x,y in dict1.items():
      if y[1]>=110:
        print(x,'优秀')
        print(dict1['Lisi'])
        a=1
        break
    else:pass
 
if a!=1:
    print('还没有这么优秀的')
  
#列表运算
list_mame=['Waiwu','Lisi','Wangwu','Zhaoliu','Zhangsan']
list_age=[18,19,20,21,22,90]
list_score=[90,80,70,60,50]
list_1=list(list_age + list_score + [100])
print(list_1)
list_1=list(list_age + list_score + [100])
print(list_1)
#列表去重  去除重复 
list_1=list(set(list_1))
print(list_1)

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list([1,2,3,4,5,6,7,8,9,10])#
list3 = list(range(1,11))
list4 = [i for i in range(1,11)]
#列表推导式
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件] 
#列表推导式：[表达式 for 变量 in 可迭代对象]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
list5 = [i for i in range(1,11) if i%2==0]
list6 = [i for i in range(1,11) if i%2!=0]
list7 = [i for i in range(1,11) if i%2==0 if i%3==0]
print(list7)
list8 = [i for i in range(1,11) if i%2==0 if i%3!=0]
print(list8)


print(list1)
print(list2)
print(list3[0:5])#切片
print(list3[-5:])#索引
print(list3[::2])#步长
print(list3[::-1])#倒序
print(list3[::-2])#倒序
print(list3[::-3])#倒序
print(list3[::-4])#倒序
print(list3[::-5])#倒序
print(list3[::-6])#倒序
print(list3[::-7])#倒序
print(list3.index(3))#索引
print(list3.count(3))#统计
list3.append(11)#追加
list3.insert(0,15)#插入
list3.extend([11,22,33])#扩展
print(list3)
list3.remove(11)#删除
#list3.pop()#删除
##list3.pop(0)#删除
#list3.clear()#清空
list3.reverse()#反转
print(list3)
list3.sort()#排序
print(list3)
list3.sort(reverse=True)#倒序
print(list3)
list3.sort(reverse=True)#排序
list3.sort(reverse=False)#排序
list3.sort(key=None,reverse=True)#排序
list3.sort(key=None,reverse=False)#排序
#移除列表中的重复元素
list3.remove(11)
list3.remove(11)#删除
list3.pop(0)#删除
del list3[0]#删除
list3.clear()#清空
list3.reverse()#反转
 #创建一个数列，后面的数字是所有数的和
list1=[1,1,2,3,5,8,13,21,34,55,89, 144, 233, 377, 610, 987, 1597, 2584, 4181]#生成式  列表生成式
list2=[x for x in range(1,101) if x%2==0]#生成式  列表生成式
list3=[x for x in range(1,101) if x%2==1]#生成式  列表生成式
list4=[x for x in range(1,101) if x%2==0 and x%3==0]#生成式  列表生成式
list5=[x for x in range(1,101) if x%2==0 and x%3==0 and x%5==0]#生成式  列表生成式


print(sum(list1))#sum函数可以求和
print(len(list1))#len函数可以求长度
 #创建一个数列，后面的数字是两个数的和
list1=[x+y for x in range(1,101) for y in range(1,x)]#生成式  列表生成式
print(list1)#len函数可以求长度
#字典的定义
dict1={'name':'张三','age':18,}#字典的定义
dict2=dict(name='张三',age=18,)#字典的定义
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
#输出字典中键值最小的键值对
dict={'LiSi':9,'waiwu':5,'lili':5}
for x,y in dict.items():
    if x == min(dict,key=dict.get):#判断x是否在字典中
       min_sum=y
for x,y in dict.items():
    if y == min_sum:
         print(x,y)
#输出字典中键值最大的键值对
dict={'LiSi':9,'waiwu':5,'lili':5,'wangwu':8,'zhaoliu':9}
for x,y in dict.items():
    if x == max(dict,key=dict.get):#判断x是否在字典中
       min_sum=y
for x,y in dict.items():
    if y == min_sum:
         print(x,y)
          
list(dict.keys())[list(dict.values()).index('张三')]#输出字典中包含的某键值的对应键
#根据最小值返回对应的键
dict={2:1,3:9,4:5}
min(dict,key=dict.get)
#根据最大值返回对应的键
dict={2:1,3:9,4:5}
max(dict,key=dict.get)
#找出所有键值为男性的键对
persons={'ZhangSan':'male',
'LiSi':'male',
'WangHong':'female'}
males = filter(lambda x:'male'== x[1], persons.items())
for (key,value) in males:
  print('%s : %s' % (key,value))


'''输出如下：

LiSi : male

ZhangSan : male

注意：

字典中的value不保证唯一性，因此根据值查出来的是一个list.

不过字典中key的值是唯一的，因此根据key将可以查到唯一的一个value'''

print('李四的性别: %s'% persons['LiSi'])

'''输出如下

李四的性别: male'''
#编写计算圆周率的程序      可以使用math库

from unicodedata import name


s=3.14
def pi(n):#定义函数
    s = 0
    for i in range(n):
        s += 1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    return s#返回值,调用函数得到s的值
n=int(input('圆周率的多边形值:'))#调用
pi(n)#调用
print(s)#3.14,自定义函数的返回值不更改S的值
print(pi(n))#3.141592653589793,调用函数的返回值
print("%.100f"%pi(n))#输出精确到小数点后位
print("%.100f"%(1/3))#输出精确到小数点后位
#自己定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-10))
#自己定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):#  判断x是否为整数或浮点数
        raise TypeError('bad operand type')#抛出异常
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-10))
#自己定义函数
def my1(x):#不可变参数
    global n1#全局变量
    n1=list(n)#将n转换为列表
    for i  in x:
      n1.send(i)#添加
    return n1#返回

m=[1,5,9,44]
n=list(m)
print(my1(m))
print(n)
print(m)
print(n1)
#自己定义函数
def my2():#不带参数
 return 'hello world'
print(my2())
#自己定义函数  可变参数 可以传入0个或多个参数 参数类型可以不同 不能传入关键字参数 不能传入可变参数 不能传入不可变参数 不能传入字典   可以传入关键字参数 可以传入可变参数  可以传入不可变参数  可以传入字典  
def my3(a,b=100):#带默认值的参数
    return a+b
print(my3(10))
print(my3(10,20))
#自己定义函数
def myfun(*args):#可变参数
    sum=0
    for i in args:
        sum+=i
    return sum
print(myfun(1,2,4,5))
#自己定义函数
def myfun(**kw):#关键字可变参数
  print(kw)
print(myfun(name='zhangsan',age=18,score=100))
#自己定义函数   
def myfun1(*a,**b):#可变参数与关键字参数 可以同时使用 可变参数必须在关键字参数之前 关键字参数必须在可变参数之后 
    print(a)
    print(b)
myfun1(1,2,3,4,5,name='zhangsan',age=18,score=100)
print(myfun1(1,2,3,4,5,name='zhangsan',age=18,score=100))
#自己定义函数
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
#系统库
import urllib #
pri