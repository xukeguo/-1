

print
#hfghfghfghfghfghghh
print ("f")

print ((5**2)**2)
print(9+6)

555555
print(9-3)
#00
'''b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()
b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()'''
#pass用于占位
a=int(input('请输入：'))
if a==1:
   pass
elif a==2:
    pass
elif a==3:
    pass
else:
    pass
#range()函数
i=range(1,10) #range(start,stop,step)
print(i)
print(list(i))
for i in range(1,10):
    print(i)
i=range(1,10,2)
for j in i:
    print(j)
#while循环
i=0 #初始化循环变量 
num_a=0  #初始化工作变量
while i<101: #循环条件
  num_a+=i #工作变量的操作（表达式）
  i+=1     #循环变量操作与定义（表达式），   循环变量的操作（表达式）与工作变量的操作（表达式）统称为循环体
print(num_a)  #循环结束后执行
#break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
#continue
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
#pass
i=0
while i<10:
    i+=1
    if i==5:
        pass
    print(i)
#for循环
for i in range(1,10):
    print(i)
#for循环
for i in range(1,10,2):
    print(i)
#for循环
for i in range(1,10,2): #多重定义，变化赋值
    print(i) 
    #累加
sum1=0
for i in range(2,101,2):
 sum1+=i #sum=sum+i sum1实现了迭代累加（累积）
print(sum1)  #2550
#累加
sum2=0
for i in range(1,101,2):
 sum2+=i
print(sum2)  #2500
sum3=sum1+sum2
print(sum3)  #5050
#累加偶数
i=0   #初始化循环变量
sum4=0  #初始化工作变量
while i<101:     #循环条件
 if i%2==0: #i%2!=0 求奇数
  sum4+=i   #sum4=sum4+i
 i+=1
print(sum4)  #2550
#累加偶数
i=0
sum5=0
while i<101:
 if not bool(i%2!=0): #bool()函数，返回值为True或False 不加not取反,求奇数
  sum5+=i
 else:
  pass
 i+=1
print(sum5)  #2550
 #累加奇数
i=0
sum6=0
while i<50:

        sum6+=i*2+1 #sum6=sum6+i*2 求偶数
    
    
        i+=1
print(sum6)  #2500
#for循环
for _ in range(1,10):
    print("hello")
for i in 'hello':
    print(i,end="\t")
#for循环
for i in [1,2,3,4,5]:
    print(i)
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

#打印水仙花数
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()#换行
#1到1000的质数
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break #跳出循环
    else:
       print(i)
    print("good")

#打印1到100的偶数
for i in range(1,100):
    if i%2!=0:
        pass   
    else:
        print(i)
#打印1到100的奇数
for i in range(1,100):
    if i%2==0:
        continue#跳出本次循环
    else:
        print(i)
#for 循环 列表 元组 字典 字符串 其他 
#for循环
for i in [1,2,3,4,5]:#列表
    print(i)

#for循环元组
for i in (1,2,3,4,5):#元组
    print(i ,end="\t")

#for循环字典
for i in {'name':'zhangsan','age':18}:#字典
    print(i)
    #for循环字符串
for i in "hello":#字符串
    print(i)
#for循环其他
for i in range(1,10):
    print(i)
    
#1到100的质数的个数
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1  
print(sum)

# 解锁
# 判断用户输入的密码是否正确
# 如果正确，则输出“登录成功”
# 如果不正确，则输出“密码错误”
# 如果用户输入的密码错误超过三次，则输出“账户锁定”
# 如果用户输入的密码正确，则输出“登录成功”
inpu = input("请输入密码：")
if inpu == "123456":
    print("登录成功")
else:
    print("密码错误")
    inpu = input("请输入密码：")
    if inpu == "123456":
        print("登录成功")
    else:
        print("密码错误")
        inpu = input("请输入密码：")
        if inpu == "123456":
            print("登录成功")
        else:
            print("密码错误")
            inpu = input("请输入密码：")
            if inpu == "123456":
                print("登录成功")
            else:
                print("密码错误")
                inpu = input("请输入密码：")
                if inpu == "123456":
                    print("登录成功")
                else:
                    print("密码错误")
                    inpu = input("请输入密码：")
                    if inpu == "123456":
                        print("登录成功")
                    else:
                        print("密码错误")
                        inpu = input("请输入密码：")
                        if inpu == "123456":
                            print("登录成功")
                        else:
                            print("密码错误")
                            inpu = input("请输入密码：")
                            if inpu == "123456":
                                print("登录成功")
                            else:
                                print("密码错误")
                                inpu = input("请输入")
      
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
inpu = int(input("请输入一个数字："))
for i in range(2,inpu):
    if inpu%i==0:
        print("不是素数")
        break
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
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break
    elif i == 2:
        print("账户锁定")
    else:
        print("密码错误")
        pwb = input("请输入密码：")
print("账户锁定")
#三 次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):  
    if pwb == "123456":
        print("登录成功")
        break
    else:
        print("密码错误")
        pwb = input("请输入密码：")                          
print("账户锁定")
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5==0:
        sum+=i
print(sum)
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5!=0:
        continue#结束本次循环
    else:
        sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break#跳出循环
    else:
        print("密码错误")
        pwb = input("请输入密码：")
        
else:
    print("账户锁定")   

    
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict={}
while True:
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    dict[name]=[age,score]
    inpu = input("是否继续（y/n）：")
    if inpu == "n":
        break
print(dict)
#创建列表
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list([1,2,3,4,5,6,7,8,9,10])
list3 = list(range(1,11))
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









      





