# coding=utf-8
#a = open("/Users/xuekguo/Documents/test.txt", "a+")
#print("http:\\\\www.baidu.com", file=a)
#a.close()   # 关闭文件
# 转义字符
print("55555\n44444")   
print("55555\b444")
print("55555\r44444")
print('55555\t44444')
print("hello\"")
print("http:\\\\www.baidu.com")
print(r"55555\n44444")
print(chr(0b10000001100111111))
print(ord('徐'))
# 导入
import keyword
from re import A  # 导入模块

print(keyword.kwlist)   # 打印模块中的关键字
name = "科国"
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
print('值', name)
n = 10
print('类型', type(n))
print('八进制', 0o755)       # 八进制
print('二进制', 0b10101111)
print('十六进制', 0x789ad)
a = 1.1
a2 = 2.1
a3 = 2.2
print(a + a2)
print(a + a3)
from decimal import Decimal   # 精度计算

print(Decimal('1.1') + Decimal('2.2'))  # 对象操作
print('八进制', 0o755)     # 八进制
print('二进制', 0b10101111)            # 二进制
print('十六进制', 0x789ad)    # 十六进制
# 求随机数
import random  
    
 

print(0)
print(random.randint(0, 10))
b = 77.77
c = True
d = False
print(str(a), type(str(a)))
print(int(b), type(str(b)))
print(int(c), type(str(c)))
# 浮点数
print(float(a), type(a))
# 字符串
print(str(a), type(str(a)))
# 整数
print(int(b), type(int(b)))
# 布尔类型
a=2
b=bool(a)
print(b, type(b))
# 布尔值
print(True, type(True))
# 字符串
print(str(a), type(str(a)))
# 浮点数
print(float(a), type(float(a)))
# 字符串
print(str(a), type(str(a)))
# 整数
print(int(b), type(int(b)))
# 布尔值
print(int(c), type(int(c)))
# 转义字符
# 换行
print("55555\n44444")
# 删除
print("55555\b444")
# 回车
print("55555\r44444")
# 制表符
print('55555\t44444')
# 转义字符
print("hello\"")
# 转义字符
print("http:\\\\www.baidu.com")
# 转义字符
print(r"55555\n44444")
# 转义字符
print(chr(0b10000001100111111))
# 转义字符
print(ord('徐'))#  转换为整数
# 转义字符
print(chr(24464))# 
# 导入
import keyword
print(keyword.kwlist)



# 数据类型-字符串
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
str1.find('c')
str2=str1.replace(str1[2],'g')# 替换  
print (str1.replace('c','g'))
print (str2)
#str1=str1[2:-3]#删除第三个到倒数第三个字符
a=str1[2:3]#第三个到第四个保留
print (a)
str1 = "hello world"  # 单个引号相当于单行文本
str.strip()  # 去除字符串两端的空格
str.lstrip()  # 去除字符串左端的空格
str.rstrip()  # 去除字符串右端的空格
str.lower()  # 将字符串转换为小写
str.upper()  # 将字符串转换为大写
str.capitalize()  # 将字符串的第一个字符转换为大写
str.title()  # 将字符串的每个单词的第一个字符转换为大写 
str.swapcase()  # 将字符串中的大写字符转换为小写，小写字符转换为大写
str.replace("hello", "world")  # 将字符串中的hello替换为world
str.find("hello")  # 查找字符串中是否包含hello，返回索引值   如果没有找到返回-1
str.count("hello")  # 返回字符串中hello的个数
str.startswith("hello")  # 判断字符串是否以hello开头
str.strip("hello")  # 去除字符串两端的hello  如果没有找到返回空字符串
str.lstrip("hello")  # 去除字符串左端的hello  如果没有找到返回空字符串
str.rstrip("hello")  # 去除字符串右端的hello  如果没有找到返回空字符串
str.title()  # 将字符串的每个单词的第一个字符转换为大写  如果没有找到返回空字符串
str.translate()  # 将字符串中的某些字符替换为其他字符  如果没有找到返回空字符串
str.endswith("hello")  # 判断字符串是否以hello结尾
str.isalnum()  # 判断字符串是否只包含字母和数字
str.isalpha()  # 判断字符串是否只包含字母
str.isdigit()  # 判断字符串是否只包含数字
str.islower()  # 判断字符串是否只包含小写字母
str.isupper()  # 判断字符串是否只包含大写字母
str.isspace()  # 判断字符串是否只包含空格
str.istitle()  # 判断字符串是否只包含单词的第一个字母
str.isascii()  # 判断字符串是否只包含ASCII字符
str.isdecimal()  # 判断字符串是否只包含十进制字符
str.isspace()  # 判断字符串是否只包含空格
str.isprintable()  # 判断字符串是否只包含可打印字符
str.isnumeric()  # 判断字符串是否只包含数字
str.join("hello")  # 将字符串拼接成新的字符串
str.split("hello")  # 将字符串按照hello分割成列表
str.partition("hello")  # 将字符串按照hello分割成元组
str.rpartition("hello")  # 将字符串按照hello分割成元组
str.rsplit("hello")  # 将字符串按照hello分割成列表
str.splitlines(True)  # 将字符串按照换行符分割成列表 保留换行符 .splitlines(True)
str.splitlines()  # 将字符串按照换行符分割成列表    如果没有换行符，则返回一个列表，列表中只有一个元素
str.split('a')  # 将字符串按照空格分割成列表           如果没有指定分隔符，默认按照空格分割
str.casefold()  # 将字符串转换为小写
str.center(20)  # 将字符串居中，并在两边填充空格
str.ljust(20)  # 将字符串左对齐，并在右边填充空格
str.rjust(20)  # 将字符串右对齐，并在左边填充空格
str.zfill(20)  # 将字符串右对齐，并在左边填充0
str.expandtabs(20)  # 将字符串中的tab符号替换为空格
str.maketrans("hello", "world")  # # 创建一个转换表
str.encode("utf-8")  # 将字符串转换为utf-8编码
str1.encode(encoding='utf-8',errors='strict') #将字符串转换成字节码
str1.decode(encoding='utf-8',errors='strict') #将字节码转换成字符串
str.decode("utf-8")  # 将字符串转换为utf-8编码
str.encode("gbk")  # 将字符串转换为gbk编码
str.decode("gbk")  # 将字符串转换为gbk编码
str.encode("ascii")  # 将字符串转换为ascii编码
str.decode("ascii")  # 将字符串转换为ascii编码
str.encode("utf-16")  # 将字符串转换为utf-16编码
str.decode("utf-16")  # 将字符串转换为utf-16编码
str.encode("utf-32")  # 将字符串转换为utf-32编码
str.decode("utf-32")  # 将字符串转换为utf-32编码
str.encode("latin-1")  # 将字符串转换为latin-1编码
str.decode("latin-1")  # 将字符串转换为latin-1编码
str.decode("gbk_2312")  # 将字符串转换为gbk_2312编码
str.encode("gbk_2312")  # 将字符串转换为gbk_2312编码
str.format_map({"name": "hello"})  # 将字符串中的{name}替换为hello
str.format()  # 将字符串中的占位符替换为参数
str.format_map()  # 将字符串中的占位符替换为参数   参数必须是字典
str.center(20, "*")  # 将字符串居中，并在两边填充字符
str.ljust(20, "*")  # 将字符串左对齐，并在右边填充字符
str.rjust(20, "*")  # 将字符串右对齐，并在左边填充字符
str.zfill(20, "*")  # 将字符串右对齐，并在左边填充字符
str.expandtabs(20, "*")  # 将字符串中的tab符号替换为字符
str.index("hello")  # 查找字符串中是否包含hello，返回索引值  如果没有找到会报错
str.partition("hello")  # 将字符串按照hello分割成元组
str.rfind("hello")  # 查找字符串中是否包含hello，返回索引值  如果没有找到会报错
str.rindex("hello")  # 查找字符串中是否包含hello，返回索引值  如果没有找到会报错
# 多行注释用三个单引号或者三个双引号，注意要用英文的引号
"""hello,
world"""

'''"""hello,
world"""'''
# 多行注释用三个单引号或者三个双引号，注意要用英文的引号
# 布尔值

str1='*'
str2 = 'hello world'
st3='*'.join(str2)#  将字符串按照*连接成新的字符串
a1=st3.split('*')#  将字符串按照*分割成列表
print(a1[3])  # 将字符串按照空格分割成列表
str2.find('e')  # 查找字符串中是否包含e，返回索引值  如果没有找到会报错
print(str2.split(' '))  # 将字符串按照空格分割成列表，并返回第三个元素

# 数据类型-整数
a = 1.1
int()#取整后创建对象
b.as_integer_ratio()#取整后返回一个元组
c.bit_length()#返回整数的二进制长度
c.conjugate()#返回复数
c.denominator()#返回分母
c.from_bytes(bytes, byteorder, signed)#从字节序列中解码整数
c.imag()#返回复数的虚数部分
c.numerator()#返回分子
c.real()#返回复数的实数部分
c.to_bytes(length, byteorder, signed)#将整数编码为字节序列
c.to_bytes_le(length)#将整数编码为小端字节序列
c.to_bytes_be(length)#将整数编码为大端字节序列
c.to_bytes_signed(length, byteorder)#将整数编码为有符号字节序列
c.to_complex()#将整数转换为复数
c.to_int()#将整数转换为整数
c.to_real()#将整数转换为实数
a.is_integer()#判断是否为整数
a.is_safe_integer()#判断是否为安全整数
a.is_finite()#判断是否为有限数
a.is_infinite()#判断是否为无穷数
a.is_nan()#判断是否为NaN
a.is_qnan()#判断是否为Quiet NaN
a.is_snan()#判断是否为Signaling NaN
a.is_signed()#判断是否为有符号数
a.is_zero()#判断是否为零
a.is_integer()#判断是否为整数
a.is_safe_integer()#判断是否为安全整数
a.is_finite()#判断是否为有限数
a.is_infinite()#判断是否为无穷数
a.is_nan()#判断是否为NaN    判断是否为NaN
a.is_qnan()#判断是否为Quiet NaN
a.is_snan()#判断是否为Signaling NaN
a=6.3
print(a.is_integer())#判断是否为整数
a.as_integer_ratio()#取整后返回一个元组  
b=663.5
b.as_integer_ratio()#取整后返回一个元组
c=99888
#取整后返回一个元组
print(c.as_integer_ratio)
c.to_bytes(4, 'little')#将整数编码为小端字节序列
print(c.to_bytes(4, 'little'))#将整数编码为小端字节序列



# 数据类型-浮点数float
float()
a.as_integer_ratio()#取整后返回一个元组  

b = 2.2586
round(b, 2)#四舍五入
print(dir(round))
b.hex()#返回十六进制表示
#保留小数点后两位 
b.fromhex # 从十六进制字符串中解码浮点数

c = 3.3
print(a)
print(b)
print(c)
# 数据类型-布尔值
bool()
   
a = True
b = False
print(a)
print(b)


a = True
b = False
#input 函数
a = input("请输入a的值：")
b = input("请输入b的值：")
print(int(a)+int(b))
#input 函数
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
print(a+b)
#input 函数
a =input("请输入a的值：")
a=int(a)
b =input("请输入b的值：")
b=int(b)
print(a**b)
#算术运算符
print(1+2)#加法
print(1-2)#减法
print(1*2)#乘法
print(1/2)#除法， 
print(1//2)#整除,公式被除数减去除数的商的整数部分
print(1%2)#取余
print(2**3)#乘方，2的3次方
#比较运算符
#等于
print(1==1)
#不等于
print(1!=1)                    # 不等于
#大于
print(1>1)         #False
print(2>1)         #True
#小于  
print(1<1)         #False
print(1<2)         #True         
#大于等于
print(1>=1)        #True
print(2>=1)        #True
#小于等于
print(1<=1)        #True
print(1<=2)        #True
#逻辑运算符
#与       
print(True and True)  #True
print(True and False) #False
print(False and False) #False                      
                         
#或
print(True or True)   #True
print(True or False)  #True
print(False or False) #False
#非    
print(not True)       #False
print(not False)      #True
#成员运算符
#in
print(1 in [1,2,3])   #True
print(6 in [1,2,3,4]) #False
#not in
print(1 not in [1,2,3])   #False 
print (8 not in [1,2,3])  #True
#身份运算符
#is
print(1 is 1)         #True
print(1 is not 1)     #False
#参数赋值运算符       #参数赋值运算符
a=20
a+=10# 相当于a=a+10
print(a)#30
a-=10# 相当于a=a-10
print(a)#20
a*=10# 相当于a=a*10
print(a)#200
a/=10# 相当于a=a/10
print(a)#20
a%=10# 相当于a=a%10
print(a)#0
a=111
a//=10# 相当于a=a//10
print(a)#11
a**=10# 相当于a=a**10   
print(a)#10000000000
a&=10# 相当于a=a&10   二进制与运算
print(a)#0
a|=10# 相当于a=a|10    二进制的或运算 
print(a)#10  
a=5
a^=10# 相当于a=a^10  二进制的异或运算
print(a)#10
a>>=10# 相当于a=a>>10
print(a)#0
a<<=10# 相当于a=a<<10
print(a)#0

#指向变量的指针
a = 10
b = a
print(b)            # 10

#**
print(2**3)#8
#指数运算符
#a^10什么意思？  
#a**10什么意思？  a的10次方
a=3
print(a^10)   
a=6
a=a|10  
print(a) 
#解包赋值
a,b,c=1,2,3
print(a,b,c,) #1 2 3   解包赋值         
#解包赋值
a,b,c=1,2,3
c,b,a=a,b,c   #交换a,b,c的值    
print(a,b,c,) #3 2 1   解包赋值
  #定义布尔类型函数  bool
#位运算符  &  |  ^  ~  <<  >>
# 位与运算符&：两个二进制数的对应位都为1，结果位就为1，否则为0。  a&b
# 位或运算符|：两个二进制数的对应位中有一个为1，结果位就为1，否则为0。  a|b
# 位异或运算符^：两个二进制数的对应位不同时，结果位就为1，否则为0。  a^b
# 位反转运算符~：对数据的每一位取反，即把1变为0，0变为1。  ~a
# 位左移运算符<<：运算数的各二进位全部左移若干位，由右边开始，其余位补0。  a<<2
# 位右移运算符>>：运算数的各二进位全部右移若干位，由左边开始，其余位补0。  a>>2
# 位移运算符  <<  >>  &  |  ^  ~  *  /  %  **  //  +=  -=  *=  /=  %=  
# **=  //=  &=  |=  ^=  <<=  >>=
#               运算符的优先级
#            ** 优先级最高，指数运算符   
#            *  /  %  优先级第二
#            +  -  优先级第三
#            <<  >>  优先级第四 
#            &  |  ^  优先级第五
#            ~  优先级第六
#            =  优先级第七
#            <  >  <=  >=  优先级第八
#            !=  ==  优先级第九
#            and  or  not  优先级第十
#            (  )  [  ]  {  }  优先级第十一
#            ,  :  ;  .  ?  =  优先级第十二
#            is  is not  in  not in  优先级第十三
#            not  and  or  优先级第十四
#            +=  -=  *=  /=  %=  **=  <<=  >>=  &=  |=  ^=  优先级第十六
#            and  or  not  优先级第十七
#以下对象的布尔值为False：
#空字符串，None，0，0.0，空列表，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象，空函数，空闭包，空类型，空模块，空类型，空元组，空字典，空集合，空字符串，空文件，空类，空对象
print (bool(''))
print (bool(None))
print (bool(0))  
print (bool(0.0))  
print (bool([]))#空列表
print (bool(())) #空元组
print (bool({})) #空字典
print (bool(set()))  #空集合
print (bool('')) #空字符串
print (bool(open('1.py')))  #空文件
print (bool(list())) #空列表
print (bool(tuple())) #空元组
print (bool(dict())) #空字典
print (bool('')) #空字符串
#以下对象的布尔值为True：
#非空字符串，非None，非0，非0.0，非空列表，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空闭包，非空类型，非空模块，非空类型，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空闭包，非空类型，非空模块，非空类型，非空元组，非空字典，非空集合，非空字符串，非空文件，非空类，非空对象，非空函数，非空
#字典的定义
dict1={'name':'张三','age':18,}#字典的定义
dict2=dict(name='张三',age=18,)
dict()#字典的定义
dict2.clear()#清空字典
dict2.copy()#复制字典
dict2.fromkeys(['name','age'])#从字典中指定的键创建新的字典
dict2.get('name')#获取字典中指定的键的值
dict2.items()#返回一个包含字典中所有键-值对的元组列表
dict2.keys()#返回一个包含字典中所有键的列表
dict2.pop('name')#删除字典中指定的键
dict2.popitem()#随机返回并删除字典中的一对键和值
dict2.setdefault('name')#设置默认值
dict2.update(dict1)#更新字典
dict2.values()#返回一个包含字典中所有值的列表
dict2.setdefault('name')#设置默认值

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


name = '张三'
age = 18
gender='男'
print('我叫%s，真的叫%s,今年%d岁,性别%s' % (name,name, age,gender)) #我叫张三，今年18岁 
print ('我叫{0}，真的叫{0},今年{1}岁,性别{2}' .format (name, age,gender))# 第二种用.format 
print (f'我叫{name}，真的叫{name},今年{age}岁,性别{gender}') # 第三用种f

'''
import builtins
print(dir(builtins))
import 
abs()#求绝对值
print(abs(-1))
aiter()#迭代器
print(aiter([1,2,3]))
print(aiter(range(1,10)))
all()#检查所有元素是否都为真
print(all([1,2,3]))
anext()#返回迭代器的下一个元素
any()#检查是否有一个元素为真
ascii()#返回一个字符串的ASCII编码
bin()#将一个整数转换为二进制表示
bool()#将对象转换为布尔值
bytearray()#创建一个新的字节数组
bytes()#创建一个新的字节数组
callable()#检查对象是否可调用
chr()#将一个整数转换为一个字符
classmethod()#创建类方法
compile()#编译Python字符串
complex()#创建一个复数
delattr()#删除属性
dict()#创建一个字典
dir()#返回一个包含当前范围内的属性和方法的字符串列表
divmod()#返回除法的余数和商
enumerate()#将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
eval()#计算表达式  可以接受一个字符串作为参数，并返回一个表达式的值
exec()#执行字符串表达式
filter()#创建一个过滤器
float()#将对象转换为浮点数
format()#格式化输出
frozenset()#创建一个不可变集合
getattr()#获取对象的属性
globals()#返回当前全局符号表
hasattr()#检查对象是否包含对应的属性
hash()#返回对象的哈希值
help()#显示帮助信息
hex()#将一个整数转换为十六进制字符串
id()#返回对象的唯一标识符
input()#获取标准输入
int()#将对象转换为整数
isinstance()#检查对象是否是一个已知的类型
issubclass()#检查对象是否是一个已知的类的子类
iter()#创建一个迭代器  可以接受一个可迭代对象作为参数，并返回一个迭代器
len()#计算对象的长度
list()#创建一个列表
locals()#返回当前的局部符号表
map()#创建一个映射
max()#返回给定参数的最大值
memoryview()#创建一个内存视图
min()#返回给定参数的最小值  
next()#返回迭代器的下一个项
object()#创建一个新的类 
oct()#将一个整数转换为八进制字符串  八进制
open()#打开一个文件
ord()#将一个字符串的第一个字符转换为一个整数
pow()#计算x的y次幂  x**y  
print()#打印一个或多个值
property()#创建一个属性
range()#创建一个序列
repr()#返回一个表示对象的字符串
reversed()#返回一个反向迭代器
round()#返回浮点数x的四舍五入值
set()#创建一个无序不重复元素集
setattr()#设置属性
slice()#创建一个切片对象
sorted()#返回一个已经排序的列表
staticmethod()#创建一个静态方法  可以接受一个函数作为参数 并返回一个函数  可以被类的实例调用 但不能被类调用  可以被类的子类调用 但不能被类的实例调用      
str()#将对象转换为字符串
sum()#求和
super()#获取父类
tuple()#创建一个元组
type()#返回对象的类型
vars()#返回对象的属性和属性值的字典
zip()#将多个序列压缩成一个序列
'''
#创建列表
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
##列表去重  去除重复 
list6=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
list6[1]=200#修改
list_1=list(set(list6))
print(list_1)
#元组
tuple1=(1,2,3,4,5,6,7,8,9,10)#元组
tuple2=(1,2,3,4,5,6,7,8,9,10)
tuple2.count(1)#统计
tuple2.index(1)#索引
del tuple2[0]#删除

#元组去重  去除重复
tuple_1=(1,2,3,4,5,5,6,6,7,8,9,10)
tuple_1.count(6)#统计
tuple_1=tuple(set(tuple_1))
print(tuple_1)
#open()
a=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','r')
b=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test1.txt','a+')
b.write(a.read())#写入
a.close()
b.close()
#read()
a=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','a+')
print(a.read())#读取

#readline()#  每次读取一行
b=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test1.txt','a+')
print(a.read(),file=b)#读取
#b.buffer()#缓冲区
#b.detach()#分离
b.close()
a.close()

     

 
     


     







 







