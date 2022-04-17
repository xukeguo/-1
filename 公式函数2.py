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

    
