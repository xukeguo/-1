

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
i=0
while i<10:
    print(i)
    i+=1
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
print(sum1)
#累加
sum2=0
for i in range(1,101,2):
 sum2+=i
print(sum2)
sum3=sum1+sum2
print(sum3)












