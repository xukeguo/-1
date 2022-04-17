#打一个烟花
def main():
    n = int(input('请输入烟花的数量：'))
    for i in range(n):
        for j in range(n-i):
            print(' ',end='')
        for k in range(i+1):
            print('*',end='')
        print()
    for i in range(n-1,-1,-1):
         for j in range(n-i):
            print(' ',end='')
         for k in range(i+1):
            print('*',end='')
         print()
main()
#圆形的烟花

#烟花的爆炸效果
def main():
    import turtle
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0,-50)
    turtle.pendown()
    turtle.pencolor('yellow')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()    
    turtle.pencolor('blue')
    turtle.circle(10)
    turtle.done()
main()
import datetime#时间模块
def main():#
    print(datetime.datetime.now())#当前时间
main()
#计算两个日期之间的天数
def main():
    import datetime
    d1 = datetime.datetime(2019,1,1)
    d2 = datetime.datetime(2019,1,2)
    print(d2-d1)
main()
#计算两个日期之间的天数
def main():
    import datetime
    d1 = datetime.datetime(2019,1,1)
    d2 = datetime.datetime(2019,1,2)
    print(d2-d1)    
main()

import email#邮件模块
#计算一个数的阶乘
def main():
    n = int(input('请输入一个数字：'))
    result = 1
    for i in range(1,n+1):
        result *= i
    print(result)
main()
#分解一个数字的质因数
def main():
    n = int(input('请输入一个数字：'))
    for i in range(2,n+1):
        while n%i == 0:
            print(i,end=' ')#end=' '表示不换行
            n = n//i
    print()
main()
#计算一个数是一定半径上的点的坐标
def main():
    import math
    r = float(input('请输入半径：'))
    n = int(input('请输入点的个数：'))
    for i in range(n):
        x = r*math.cos(2*math.pi*i/n)
        y = r*math.sin(2*math.pi*i/n)
        print('第%d个点的坐标为（%.2f,%.2f）'%(i+1,x,y))
main()
#用枚举类型来表示一个月份
def main():
    import enum
    class Month(enum.Enum):
        Jan = 1
        Feb = 2
        Mar = 3
        Apr = 4
        May = 5
        Jun = 6
        Jul = 7
        Aug = 8
        Sep = 9
        Oct = 10
        Nov = 11
        Dec = 12
    m = int(input('请输入一个月份：'))
    if m in [i.value for i in Month]:
        print(Month(m).name)
    else:
        print('输入有误')
main()
#用枚举类型来表示一个星期
def main():
    import enum
    class Week(enum.Enum):
        Sun = 1
        Mon = 2
        Tue = 3
        Wed = 4
        Thu = 5
        Fri = 6
        Sat = 7
    w = int(input('请输入一个星期：'))
    if w in [i.value for i in Week]:
        print(Week(w).name)
    else:
        print('输入有误')
main()
#用枚举类型来表示一个季节
def main():
    import enum
    class Season(enum.Enum):
        Spring = 1
        Summer = 2
        Autumn = 3
        Winter = 4
    s = int(input('请输入一个季节：'))
    if s in [i.value for i in Season]:
        print(Season(s).name)
    else:
        print('输入有误')
main()
#用枚举法解决一元二次方程
def main():
    import math
    a = float(input('请输入a：'))
    b = float(input('请输入b：'))
    c = float(input('请输入c：'))
    if a == 0:
        if b == 0:
            if c == 0:
                print('无解')
            else:
                print('无穷多个解')
        else:
            print('x = %.2f'%(-c/b))
    else:
        delta = b**2-4*a*c
        if delta < 0:
            print('无解')
        elif delta == 0:
            print('x = %5.2f'%(-b/(2*a)))
        else:
            print('x1 = %.2f'%((-b+math.sqrt(delta))/(2*a)),end=' ')
            print('x2 = %.2f'%((-b-math.sqrt(delta))/(2*a)))
main()
#用枚举法解决a*b*c的最大公约数
def main():
    import math
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    c = int(input('请输入c：'))
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    if a == b:
        print('%d'%c)
    elif a == c:
        print('%d'%b)
    elif b == c:
        print('%d'%a)
    else:
        for i in range(a,0,-1):
            if a%i == 0 and b%i == 0 and c%i == 0:
                print('%d'%i)
                break
main()

#用枚举法解决a*b的最小公倍数
def main():
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    for i in range(a*b,0,-1):
        if a%i == 0 and b%i == 0:
            print('%d'%i)
            break
main()

def main():
    import enum
    class 国家(enum.Enum):
        中国 = 1
        美国 = 2
        日本 = 3
        韩国 = 4
        德国 = 5
        法国 = 6
        英国 = 7
        意大利 = 8
        印度 = 9
        台湾 = 10
        泰国 = 11
        西班牙 = 12
        马来西亚 = 13
        越南 = 14
        澳大利亚 = 15
        印度尼西亚 = 16
        其他 = 17
    n = int(input('请输入一个国家：'))
    if n in [i.value for i in 国家]:
        print(国家(n).name)
    else:
        print('输入有误')
main()
    
    #用枚举法解决一个数字的百位数
def main():
    n = int(input('请输入一个数字：'))
    print(n//100)
main()
#解决x*y=c,x+y=d的 非整数解
#不import lib
def main():
    import fpdf 
    import math
    
  



