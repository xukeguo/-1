#编写计算圆周率的程序      可以使用math库
#自己定义函数
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
def my1(x):
    n1=list(n)#将n转换为列表
    for i  in x:
      n1.append(i)#添加
    return n1#返回

m=[1,5,9,44]
n=list(m)
print(my1(m))
print(n)
print(m)
#自己定义函数
def my2():
 return 'hello world'
print(my2())


