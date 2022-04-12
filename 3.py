#编写计算圆周率的程序      可以使用math库
#自己定义函数
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
   # global n1#全局变量
    n1=list(n)#将n转换为列表
    for i  in x:
      n1.append(i)#添加
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
print(fun(1,2,4,5))
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
#字典的使用的查找  字典的使用的添加  字典的使用的删除  字典的使用的修改
dict1={'name':'zhangsan','age':18,'score':100}
print(dict1['name'])
print(dict1['age'])
print(dict1['score'])
dict1['name']='lisi'   #修改 
print(dict1['name'])
# 输出字典中的包含某个值的所有键  
print(dict1.keys())
# 输出字典中的包含某个值的所有值
print(dict1.values())
# 输出字典中包含的某键值的对应键
#print字典中包含的某键值的对应键  筛选

dict={'name':'张三',3:9,4:5}
list(dict.keys())[list(dict.values()).index('张三')]
lis1=list(dict.values()).index('张三')
print(lis1)
#输出字典中包含的某键值的对应键
#根据最小值返回对应的键
dict={2:1,3:9,4:5}
min(dict,key=dict.get)
#根据最大值返回对应的键
dict={2:1,3:9,4:5}
max(dict,key=dict.get)
#找出所有键值为男性的键对 字典的筛选的查找
persons={'ZhangSan':'male',
'LiSi':'male',
'WangHong':'female'}
males = filter(lambda x:'male'== x[1], persons.items())
print(males,type(males)) 
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
#找出所有键值为男性的键对 字典的筛选的查找 用for  in  语句
persons={'ZhangSan':'male','LiSi':'male','WangHong':'female'}
dict1={x:y for x,y in persons.items()}
print(dict1)  
for x,y in persons.items():
    if y=='male':
        print(x,y)

#找数列 最大数
list1=[1,5,5,9,11,88,102]
sum=-100#若干小
for i in list1:
    if i> sum:
        sum=i
print(sum)
#数列的和
list1=[1,5,5,9,11,88,102]
sum=0
for i in list1:
    sum+=i
print(sum)

#建立一个数列，求出数列的和 和的平方  和的立方  和的平方根 和的立方根  
list1=[1,5,5,9,11,88,102]
sum=0
for i in list1:
    sum+=i
print(sum)
print(sum**2)
print(sum**3)
print(sum**0.5)
print(sum**(1/3))
#建立一个数列，后面的数列的值为前面的数列的值的两倍
list1=[1,5,5,9,11,88,102]
list2=[]
for i in list1:
    list2.append(i*2)
print(list2)

#建立一个数列，后面为前面的数的值的和
list1=[1,1,2,4]
sum=0
sum2=0
i=2
while sum2<100:
    #list2=list1[i:]
    for i in list1:
      sum+=i
    list1.append(sum)
    sum2=sum
    sum=0
    i=i+1
print(list1)










