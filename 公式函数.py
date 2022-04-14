print(bool(6==7))#判断是否相等
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
inpu = int(input("请输入一个数字："))
for i in range(2,inpu):
    if inpu%i==0:
        print("不是素数")
        break #跳出循环
else:
     print("是素数")
#包含1到100的质数的集合
dict={}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            ge = i#获取质数
            dict[ge]=ge
print(dict)
#1到100的质数的和
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)
#1到100的质数的和
sum=0
for i in dict:
  sum+=i
print(sum)
#素数 逆向思维 
    #素数 逆向思维 判定条件一
dict1={}
for i in range(2,101):
    dict1[i]=True
    for j in range(2,i):
        if i%j==0:
            dict1[i]=False
            break
    else:
        dict1[i]=True 
print(dict1)
    #素数 逆向思维 判定条件二
set1={x for x in range(2,100)}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
          set1.discard(i)
print(set1)

list1=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        list1.append(i) 
        
print(list1)

       
#素数 正向思维
dict1={}
for i in range(2,101):
    dict1[i]=True 
for i in range(2,101):
    for j in range(i*2,101,i):
      dict1[j]=False
print(dict1)
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
list2=[x*y for x in range(1,101) for y in range(1,101) if x==y]#生成式  列表生成式
list3=[x*y for x in range(1,101) for y in range(1,101) if x>y]#生成式  列表生成式
list4=[x*y for x in range(1,101) for y in range(1,101) if x>y and x%y==0]#生成式  列表生成式
list1=[1,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]#生成式是：
#创建一个数列，后面的数字是两个数的和
list1=[1,1]
for i in range(2,15):
    list1.append(list1[-1]+list1[-2])#索引取值
print(list1)
#创建一个数列，后面的数字的两倍
list1=[1,2]
for i in range(2,7):
    list1.append(list1[-1]*2)#索引取值
print(list1)
#创建一个数列，后面的数字的两倍
list1=['a','b','c','d','e','f']
list2=[1,2,4,8,16,32,64]
dict1={x:y for x,y in zip(list1,list2)}
print(dict1)

#递归函数
def fact(n):
    if n==2:
        return 1
    return 2*fact(n-2)
print(fact(8))

def fact(n):
    return fact_iter(n,2)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(5))

#翡波那契数列
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

list1=[1,1,2]
for i in range(3,10):
    list1.append(list1[-1]+list1[-2])
print(list1)
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
#打印水仙花数
for i in range(100,1000,1):#初始为100，终止为1000，步长为1
    a=i//100 #取百位数
    b=i%100//10#//取整除法（i//10%10）
    c=i%10  #取个位数
    if i==a**3+b**3+c**3:
        print(i)


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
def myfun2(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
#求最大值
#求两数的最大公约数
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
for i in range(a+b,1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
else:
    print('没有公约数')
#求两数的最小公位数
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break



def max(list):#求最大值
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
#因式分解

def my_factor(n):
    b=n
    a=0
    for i in range(2,n):
        if n%i==0:
            for j in range(1,b):
                if n%i!=0:
                 break
                else:
                    print(i)
                    list8.append(i)           
                    n=n/i
                    a=1
   
    if a==0:
      print('%d是素数'%b)
    else:
      print('%d的因式分解为%s'%(b,list8))
      return list8
list8=[]        
n=int(input('请输入一个数字:'))
print(my_factor(n))
print(list8)
