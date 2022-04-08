#取款  
monry=10000000   #账户余额
print('取款')
s=int(input('请输入取款金额：'))  #取款金额
if s>monry: #如果取款金额大于账户余额
    print('余额不足')   #余额不足
else:#分支  如果取款金额小于账户余额
    monry=monry-s #账户余额减去取款金额
    print('取款成功，余额为：',monry) #取款成功，输出余额
    存款
    print('存款')
    s=int(input('请输入存款金额：'))  #存款金额
    monry=monry+s #账户余额加上存款金额
    print('存款成功，余额为：',monry) #存款成功，输出余额
    #输出
    print('输出')
    print('你好')
    print('你好','你好')

    #输入
    print('输入')





# 取款
# monry=10000000   #账户余额
# print('取款')
# s=int(input('请输入取款金额：'))  #取款金额
# if s>monry: #如果取款金额大于账户余额
#    print('余额不足')   #余额不足
# else:
#   monry=monry-s #账户余额减去取款金额
#  print('取款成功，余额为：',monry) #取款成功，输出余额
#  #取款
#     多分支if-else
score=int(input('请输入分数：'))
if score>=90:
    print('优秀')
elif score>=80:
    print('良好')  
elif score>=70:
    print('中等')
elif score>=60:
    print('及格')
else:  
    print('不及格')
         
#     多分支if-else
score=int(input('请输入成绩：'))
if score>=90 and score<=100:
    print('优秀')
elif score>=80 and score<=89:
    print('良好')
    print('良好')
elif score>=70 and score<=79:
    print('中等')
elif score>=60 and score<=69:
    print('及格')
elif score>=0 and score<=59:
    print( '不及格')
else:
    print('输入错误')
    #     多分支if-else
score=int(input('请输入成绩：'))
if 90<=score>=100:
    print('优秀')
elif 80<=score>=89:
    print('良好')
elif 70<=score>=79:
    print('中等')
elif 60<=score>=69:
    print('及格')
elif 0<=score>=59:
    print('不及格')
else:
    print('输入错误')
    #     多分支if-else
    #嵌套if-else
#判断是否为会员
#会员等级
#普通会员
#银牌会员
#金牌会员
#钻石会员
#输入
answer=input('是否为会员?：y/n')
money=float(input('请输入金额：'))
if answer=='y' or answer=='Y':
    if 2000>=money>=1000:
        print('普通会员') #普通会员
    elif  3000>= money>=2000:
        print('银牌会员')
    elif 4000>=money>=3000:
        print('金牌会员')
    elif money>=4000:
        print('钻石会员')
    else:
        print('输入错误')
else:
    print('输入错误')
    #嵌套if-else
#判断是否为会员
answer=input('是否为会员?：y/n')
money=float(input('请输入金额：'))
if answer=='Y' or answer=='y':
    if money>=5000:
        print('钻石会员五折',money*0.5)          
    elif money>=4000:
        print('金牌会员六折',money*0.6)
    elif money>=3000:
        print('银牌会员七折',money*0.7)
    elif money>=2000:
        print('普通会员八折',money*0.8)
    elif money>=1:
        print('普通会员九折',money*0.9)
    else:
        print('普通会员',money)
elif answer=='N' or answer=='n':
    print('普通会员',money)
else:
    print('输入错误')
    #黑白名单
    name=input('请输入姓名：')
    if name in ['张三','李四','王五']:#判断是否为黑名单
        print('黑名单') #黑名单
    else: #不是黑名单
        print('白名单') #白名单

    
    