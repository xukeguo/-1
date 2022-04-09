

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
for i in range(100,1000):
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
for i in range(2,10000):
    for j in range(2,i):
        if i%j==0:
            break #跳出循环
    else:
        print(i)

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





