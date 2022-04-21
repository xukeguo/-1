#我的列表类
from curses import meta
from multiprocessing.sharedctypes import Value
from re import T#导入Value类


class Mylist:
    #def __init__(self, value):
       # self.value = value
       # self.next = None
        pass
class Mylist(list):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
        self.next = None
    def my_avg(self):
            sum = 0
            for i in self:
                sum += i
            return sum / len(self)
    def my_max(self):
        max = self[0]
        for i in self:
            if i > max:
                max = i
        return max
    def my_min(self):
        min = self[0]
        for i in self:
            if i < min:
                min = i
        return min
    def my_sum(self):
        sum = 0
        for i in self:
            sum += i
        return sum
    def my_len(self):
        return len(self)
    def my_av(self):
        return sum(self)/len(self)
    def my_append(self, value):
        self.append(value)
    def my_insert(self, index, value):#插入
        self.insert(index, value)
    def my_remove(self, value):
        self.remove(value)
    def my_pop(self, index):
        self.pop(index)
    def my_index(self, value):
        return self.index(value)
    def my_count(self, value):
        return self.count(value)
    def my_sort(self):
        self.sort()
    def my_reverse(self):
        self.reverse()
    def my_clear(self):
        self.clear()
    def my_copy(self):
        return self.copy()
    def my_extend(self, value):
        self.extend(value)
    def my_count(self, value):
        return self.count(value)
    def my_count(self, value):
        return self.count(value)
    def my_count(self, value):
        return self.count(value)
lis=Mylist([1,2,3,4,5])
print(lis.my_avg())
lis.append(6)
print(lis.my_av())
print(sum(lis))
print(lis.my_sum())



#!/usr/bin/env python3
# Path: 类.py
#我的数据类型

class Myint:
    
    pass
class Myint(int):
    '''def __init__(self, value):
        super().__init__(value)
        self.value = value'''
    def my_abs(self):
        if self >= 0:
            return self
        else:
            return -self
    def my_lt(self, value):
        return self < value
    def my_rtruediv(self, value):
        return value / self
    def my_zfill(self, value):
        return self.zfill(value)
    def my_prime(self):#质因数分解
        list_zysfj=[]    
        b=self
        for i in range(2,self+1):
              for j in range(2,b+1):
                if self%i!=0:
                 break
                else:
                   # print(i)
                    list_zysfj.append(i)           
                    self=self/i
        global c
        c=list_zysfj
        #print('%d的因式分解为%s'%(b,c))#%s是字符串 %d是整数  %f是浮点数 %.2f是保留两位小数 %.3f是保留三位小数 
        return c
    def my_add(self, value):
        return self + value
    def my_sub(self, value):
        return self - value
    def my_mul(self, value):
        return self * value
    def my_div(self, value):
        return self / value
    def my_mod(self, value):
        return self % value
    def my_pow(self, value):
        return self ** value
    def my_floordiv(self, value):
        return self // value
    def my_truediv(self, value):
        return self / value
    def my_invert(self):
        return -self
    def my_lshift(self, value):
        return self << value
    def my_rshift(self, value):
        return self >> value
    def my_and(self, value):
        return self & value
    def my_or(self, value):
        return self | value
    def my_xor(self, value):
        return self ^ value
    def my_radd(self, value):
        return value + self
    def my_rsub(self, value):
        return value - self
    def my_rmul(self, value):
        return value * self
    def my_rdiv(self, value):
        return value / self
    def my_rmod(self, value):
        return value % self
    def my_rpow(self, value):
        return value ** self
    def my_rfloordiv(self, value):#取整除
        return value // self
    def my_rtruediv(self, value):#真除
        return value / self
    def my_rlshift(self, value):# 左移
        return value << self
    def my_rrshift(self, value):#右移
        return value >> self
    def my_pos(self):#正数
        return +self
    def my_neg(self):#负数
        return -self
    def my_isprime(self):#是否为素数
        for i in range(2,self):
         if self%i==0:
            return False
        else:
         return True



a=Myint(97)
b=5
c=756
c=Myint(c)
print(Myint.my_prime(c))
print(a.my_prime())
print(Myint(b).my_prime())
print(Myint.my_isprime(107))
#print(Myint.my_zysfj(c))
#我的字典类型
class Mydict:
    pass
class Mydict(dict):
    def my_get(self, key):#获取
        return self.get(key)
    def my_set(self, key, value):#设置
        self.set(key, value)
    def my_items(self):
        return self.items()
    def my_keys(self):
        return self.keys()
    def my_values(self):
        return self.values()
    def my_pop(self, key):#删除
        return self.pop(key)
    def my_popitem(self):#随机删除
        return self.popitem()
    def my_update(self, value):
        self.update(value)
    def my_clear(self):
        self.clear()
    def my_copy(self):
        return self.copy()
    def my_fromkeys(self, value):
        return self.fromkeys(value)
    def my_get(self, key):
        return self.get(key)
    def my_setdefault(self, key, value):#设置默认值
        return self.setdefault(key, value)
    def my_fromkeys(self, value):
        return self.fromkeys(value)
    def my_get(self, key,default=None):
        return self.get(key)
    def my_setdefault(self, key, value):
        return self.setdefault(key, value)
    def my_pop(self, key):
        return self.pop(key)
    def my_popitem(self):
        return self.popitem()
    def my_update(self, value ):
        self.update(value)
    def my_clear(self):
        self.clear()
    def my_maxx(self):
        for i, j in self.items():
           if i == max(self):  # 判断x是否在字典中
              sum1 = j
        for i, j in self.items():
           if j == sum1:
               print(i, j)

    def my_minx(self):
        for x, y in self.items():
           if x == min(self):
                min_sum = y
        for x, y in self.items():
           if y == min_sum:
              print(x, y)
    def my_find(self, value):
        for i, j in self.items():
            if j == value:
                print(i, j)
    def my_find_all(self, value):
        for i, j in self.items():
            if j == value:
                print(i, j)
    def my_find_all_key(self, value):
        for i, j in self.items():
            if i == value:
                print(i, j)
    def my_filter(self, value):
        for i, j in self.items():
            if j == value:
                print(i, j)

    
dic=Mydict({'a':1,'b':1,'c':3,'d':5,'e':5})
name_dic=list({'zhangsan','lisi','wangwu','zhaoliu','zhaoliu'})
age_dict=list({15,20,25,30,35})
scor_dic=list({88,88,100,90,100})
dict2=Mydict({x:[y,z] for x,y,z in zip(name_dic,age_dict,scor_dic)})
print(dic.my_get('a'))
print(dic.my_get('d',5))
print(dic.my_get('f'))
print(max(dic))
dic.my_maxx()
dic.my_find(1)

#我的filter类型
class Myfilter:
    pass
class Myfilter(filter):
    def __init__(self, func, iterable):
       super().__init__(func, iterable)
       filter.__init__(self, func, iterable)

    def my_filter(self, value):
        return self.filter(value)
    def my_map(self, value):
        return self.map(value)
    def my_reduce(self, value):
        return self.reduce(value)
    def my_zip(self, value):
        return self.zip(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)
    def my_tuple(self, value):
        return self.tuple(value)
    def my_set(self, value):
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):
        return self.any(value)
    def my_all(self, value):#判断是否全部为真
        return self.all(value)
    def my_enumerate(self, value):#枚举
        return self.enumerate(value)
    def my_reversed(self, value):#反转
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):#转换为列表
        return self.list(value)
    def my_tuple(self, value):#转换成元组
        return self.tuple(value)
    def my_set(self, value):#集合
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):#判断是否有真值
        return self.any(value)
    def my_all(self, value):#判断是否全部为真
        return self.all(value)
    def my_enumerate(self, value):#枚举
        return self.enumerate(value)
    def my_reversed(self, value):
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)

#我的map类型
class Mymap:
    pass
class Mymap(map):

    def my_map(self, value):
        return self.map(value)
    def my_filter(self, value):
        return self.filter(value)
    def my_reduce(self, value):
        return self.reduce(value)
    def my_zip(self, value):
        return self.zip(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)
    def my_tuple(self, value):
        return self.tuple(value)
    def my_set(self, value):
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):
        return self.any(value)
    def my_all(self, value):
        return self.value
    def my_enumerate(self, value):
        return self.enumerate(value)
    def my_reversed(self, value):
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)
    def my_tuple(self, value):
        return self.tuple(value)
    def my_set(self, value):
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):
        return self.any(value)
    def my_all(self, value):
        return self.all(value)
    def my_enumerate(self, value):
        return self.enumerate(value)
    def my_reversed(self, value):
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)

#我的reduce类型

    def my_map(self, value):
        return self.map(value)
    def my_filter(self, value):
        return self.filter(value)
    def my_reduce(self, value):
        return self.reduce(value)
    def my_zip(self, value):
        return self.zip(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)
    def my_tuple(self, value):
        return self.tuple(value)
    def my_set(self, value):
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):
        return self.any(value)
    def my_all(self, value):
        return self.all(value)
    def my_enumerate(self, value):
        return self.enumerate(value)
    def my_reversed(self, value):
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)
    def my_list(self, value):
        return self.list(value)
    def my_tuple(self, value):
        return self.tuple(value)
    def my_set(self, value):
        return self.set(value)
    def my_sum(self, value):
        return self.sum(value)
    def my_any(self, value):
        return self.any(value)
    def my_all(self, value):
        return self.all(value)
    def my_enumerate(self, value):
        return self.enumerate(value)
    def my_reversed(self, value):
        return self.reversed(value)
    def my_sorted(self, value):
        return self.sorted(value)
#我的set类型
class Myset:
    pass
class Myset(set):

    
        def my_map(self, value):#map
            return self.map(value)
        def my_filter(self, value):#filter
            return self.filter(value)
        def my_reduce(self, value):
            return self.reduce(value)
        def my_zip(self, value):
            return self.zip(value)
        def my_sorted(self, value):
            return self.sorted(value)
        def my_list(self, value):
            return self.list(value)
        def my_tuple(self, value):
            return self.tuple(value)#元组
        def my_set(self, value):
            return self.set(value)
        def my_sum(self, value):
            return self.sum(value)
        def my_any(self, value):#判断是否有真值
            return self.any(value)
        def my_all(self, value):#判断是否全部为真
            return self.all(value)
        def my_enumerate(self, value):#枚举
            return self.enumerate(value)
        def my_reversed(self, value):
            return self.reversed(value)
        def my_sorted(self, value):
            return self.sorted(value)
        def my_list(self, value):
            return self.list(value)
        def my_tuple(self, value):
            return self.tuple(value)
        def my_set(self, value):
            return self.set(value)
        def my_sum(self, value):#求和
            return self.sum(value)
        def my_any(self, value):
            return self.any(value)
        def my_all(self, value):
            return self.all(value)
        def my_enumerate(self, value):
            return self.enumerate(value)
        def my_reversed(self, value):
            return self.reversed(value)
        def my_sorted(self, value):
            return self.sorted(value)
        def my_list(self, value):#我的list类型
            return self.list(value)
a=Myset([1,4,3,6]+[2,5,7])
print(a.add(7))
print(a.remove(4))
print(a)

class my:
    def __new__(cls, *args, **kwargs):
        return super().__new__(  cls )

    def __init__(self,value,name,age):
        self.value=value
        self.name=name
        self.age=age
    def my_map(self, value1):
        return self.value+5
      
a=my(1,'a',18)
print(a.my_map(5))      
#类的继承
class persons(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self,name,age):#
        return 'name:%s,age:%s'%(self.name,self.age)#
    def info (self):
        print('name:%s,age:%s'%(self.name,self.age))
class student(persons):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def infostu(self):
        print('name:%s,age:%s,score:%s'%(self.name,self.age,self.score))
    def info1(self):
        super().info()
        print('score:%s'%(self.score))

class teacher(persons):
    def __init__(a,name,age,salary):
        super().__init__(name,age)
        a.salary=salary
    def infotea(a):
        print('name:%s,age:%s,salary:%s'%(a.name,a.age,a.salary))
a=student('a',18,100)
a.info()
a.info1()
a.infostu()
b=teacher('b',38,1000)
#f=teacher(b)

#b.info
b.infotea()
#多态
class Animal:
    def run(self):
        print('Animal is running')  
class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running')
class Runnable:
    def run(self):
        print('Running...')
class TortoiseRunnable(Runnable,Tortoise):
    pass
class CatRunnable(Cat,Runnable):
    pass
class DogRunnable(Dog,Runnable):
    pass
#

a=Animal()    
b=Animal() 
a.run()
b=CatRunnable()
b.run()
c=DogRunnable()
c.run()
def fun(object):
    object.run()
fun(a)


#__new__方 法
class A:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)
    def __init__(self):
        print('__init__')
a=A()
#__new__方法
#继承不可变数据类型时，可以重写__new__方法，返回一个新的对象，而不是原来的对象
#（like int str or tuple）
class Inch(float):
    def __new__(cls, arg=0.0):
        a=12*arg
        return a
        return super().__new__(cls, 12 * arg)
        return float.__new__(cls, arg*0.0254)
b=float(1.5)

a=Inch(b)
c=Inch(a)
print(c)
print(a)
#用在元类，定制类对象
class MetaClass(type):#元类
    def __new__(cls, meta,name, bases, attrs):#meta是元类，name是类名，bases是父类，attrs是属性
        print('__new__')
        return super(MetaClass,meta).__new__(cls, meta,name, bases, attrs)#返回一个新的类对象
    def __init__(cls,name, bases, attrs):#name是类名，bases是父类，attrs是属性
        print('__init__')
        super(MetaClass,cls).__init__(name, bases, attrs)#返回一个新的类对象
class Meclass(object):
    __metaclass__=MetaClass#元类
    def foo(self,param):
        print('foo',param)
p=Meclass()
p.foo('hello')
        
'''__new__的作用
__new__方法的作用是，创建并返回一个实力对象，如果__new__只调用了一次，就会得到一个对象，继承自object的新式类才有new这一魔法方法
注意事项
__new__是在一个对象实例化的时候所调用的第一个方法
__new__至少必须要有一个参数cls，代表要实例化的类，此参数在实例化时由python解释器自动提供，其他的参数时用来直接传递给__init__方法
__new__决定是否要使用该__init__方法，因为__new__可调用其他类的构造方法或者直接返回别的实力对象来作为本类的实例，如果__new__没有返回实例对象，则__init__不会被调用
在__new__方法中，不能调用自己的__new__方法，即：return cls.__new__(cls)，否则报错（Recursionerror：maximum recursion depth exceeded：超过最大递归深度）
实例

复制代码'''
class Animal(object):
  
    def __init__(self):
        self.color = color
    #如果不重写，__new__默认结构如下
    def __new__(cls,*args,**kwargs):
        return super().__new__(cls,*args,**kwargs)
        #return object.__new__(cls,*args,**kwargs)
tigger = Animal() #实例化过程中会自动调用__new__
'''复制代码
在新式类中__new__才是真正的实例化方法，为类提供外壳制造出实例框架，然后调用框架内的构造方法__init__进行操作

我们可以将类比作制造商，__new__()方法就是前期的原材料购买环节，__init__()方法就是在有原材料的基础上，加工，初始化商品环节。

单例模式

是一种常用的软件设计模式，目的：确保某一个类只有一个实例存在

如果希望在某个系统中，某个类只能出现一个实例的时候，那么这个单例对象就能满足要求

复制代码'''
class DatabaseClass(object):
    def __new__(cls, *args, **kwargs):
        # cls._instance=cls.__new__(cls) 不能使用自身的new方法
        #容易造成一个深度递归，应该调用父类的new方法
        if not hasattr(cls,'_instance'):#判断是否有_instance属性
            cls._instance=super().__new__(cls, *args, **kwargs)###调用父类的new方法
        return cls._instance

    pass

db1 = DatabaseClass()
print(id(db1))

db2 = DatabaseClass()
print(id(db2))

db3 = DatabaseClass()
print(id(db3))
'''_new__的作用
__new__方法的作用是，创建并返回一个实力对象，如果__new__只调用了一次，就会得到一个对象，继承自object的新式类才有new这一魔法方法
注意事项
__new__是在一个对象实例化的时候所调用的第一个方法
__new__至少必须要有一个参数cls，代表要实例化的类，此参数在实例化时由python解释器自动提供，其他的参数时用来直接传递给__init__方法
__new__决定是否要使用该__init__方法，因为__new__可调用其他类的构造方法或者直接返回别的实力对象来作为本类的实例，如果__new__没有返回实例对象，则__init__不会被调用
在__new__方法中，不能调用自己的__new__方法，即：return cls.__new__(cls)，否则报错（Recursionerror：maximum recursion depth exceeded：超过最大递归深度）
实例

复制代码'''
class Animal(object):
  
    def __init__(self):
        self.color = color
    #如果不重写，__new__默认结构如下
    def __new__(cls,*args,**kwargs):
        return super().__new__(cls,*args,**kwargs)
        #return object.__new__(cls,*args,**kwargs)
tigger = Animal() #实例化过程中会自动调用__new__
'''复制代码
在新式类中__new__才是真正的实例化方法，为类提供外壳制造出实例框架，然后调用框架内的构造方法__init__进行操作

我们可以将类比作制造商，__new__()方法就是前期的原材料购买环节，__init__()方法就是在有原材料的基础上，加工，初始化商品环节。

单例模式

是一种常用的软件设计模式，目的：确保某一个类只有一个实例存在

如果希望在某个系统中，某个类只能出现一个实例的时候，那么这个单例对象就能满足要求

复制代码'''
class DatabaseClass(object):
    def __new__(cls, *args, **kwargs):
        # cls._instance=cls.__new__(cls) 不能使用自身的new方法
        #容易造成一个深度递归，应该调用父类的new方法
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls, *args, **kwargs)
        return cls._instance

    pass

db1 = DatabaseClass()
print(id(db1))

db2 = DatabaseClass()
print(id(db2))

db3 = DatabaseClass()
print(id(db3))
'''复制代码
 

1、__new__方法默认返回实例对象供__init__方法、实例方法使用。

复制代码'''
class Foo(object):
    '''黄哥python培训，黄哥所写'''
    price = 50

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo = Foo()
print(foo.how_much_of_book(8))
print(dir(Foo))
'''复制代码
分析上面的代码，这个类实例化过程，Foo类继承object类，继承了object的__new__方法。

当你没有重写这个方法(通俗来说，你没有在Foo类中没有定义__new__方法)，Foo实例化是默认自动调用父类__new__方法，这个方法返回值为类的实例(self),提供这个函数how_much_of_book，默认的第一个参数self。

复制代码'''
class Foo(object):
    price = 50

    def __new__(cls, *agrs, **kwds):
        inst = object.__new__(cls, *agrs, **kwds)
        print(inst)
        return inst


    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo = Foo()
print(foo.how_much_of_book(8))
# <__main__.Foo object at 0x1006f2750>
# <__main__.Foo object at 0x1006f2750>
# 400
'''复制代码
请看上面代码，Foo类中重载了__new__方法，它的返回值为Foo类的实例对象。

2、__init__ 方法为初始化方法，为类的实例提供一些属性或完成一些动作。

复制代码'''
class Foo(object):

    


    def __init__(self, price=40):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo = Foo()
print(foo.how_much_of_book(8))

# <__main__.Foo object at 0x1006f2750>
# <__main__.Foo object at 0x1006f2750>
# 400
'''复制代码
3、__new__ 方法创建实例对象供__init__ 方法使用，__init__方法定制实例对象。

__new__ 方法必须返回值，__init__方法不需要返回值。(如果返回非None值就报错)

 

4、一般用不上__new__方法，__new__方法可以用在下面二种情况。

__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

继承不可变数据类型时需要用到__new__方法(like int, str, or tuple） 。'''

class Inch(float):
    "Convert from inch to meter"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)

print(Inch(12))
'''用在元类，定制创建类对象

复制代码'''



# -----------------------------------
# Allocating memory for class Myclass
# <class '__main__.MetaClass'>
# (<type 'object'>,)
# {'__module__': '__main__', 'foo': <function foo at 0x1007f6500>, '__metaclass__': <class '__main__.MetaClass'>}
# -----------------------------------
# Initializing class Myclass
# <class '__main__.Myclass'>
# (<type 'object'>,)
# {'__module__': '__main__', 'foo': <function foo at 0x1007f6500>, '__metaclass__': <class '__main__.MetaClass'>}
# hello
'''复制代码
 一个比较实际的例子，是在Django admin 表单验证的时候如何访问当前请求request。StackFlow的链接如下： http://stackoverflow.com/questions/1057252/how-do-i-access-the-request-object-or-any-other-variable-in-a-forms-clean-met/6062628#6062628

首先想到的是把request也传递过去，在clean方法就可以使用了。

复制代码'''
#‘’一个比较实际的例子，是在Django admin 表单验证的时候如何访问当前请求request。StackFlow的链接如下： http://stackoverflow.com/questions/1057252/how-do-i-access-the-request-object-or-any-other-variable-in-a-forms-clean-met/6062628#6062628

#首先想到的是把request也传递过去，在clean方法就可以使用了。’‘’

#复制代码‘’‘
from urllib import request
from django import forms
class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(MyForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        #这里可以得到self.request的信息
        pass

f = MyForm(request.POST, request=request)
#但是在定制ModelAdmin的时候却不行，因为admin只提供get_form这个方法，返回值是类对象，而不是实例对象

    #get_form(self, request, *args, **kwargs):
        # 这行代码是错误的
        # return MyForm(request=request) 
       # return MyForm     # OK
#用__new__方法可以解决这个问题。

def get_form(self, request, *args, **kwargs):
    class ModelFormMetaClass(MyForm):
        def __new__(cls, *args, **kwargs):
            kwargs['request'] = request
            return MyForm(*args, **kwargs)
    return ModelFormMetaClass
那么结果如何呢，add_view的调用代码如下：

复制代码
def add_view(self, request, form_url='', extra_context=None):
'''    "The 'add' admin view for this model."
    model = self.model
    opts = model._meta

    if not self.has_add_permission(request):
        raise PermissionDenied

    ModelForm = self.get_form(request)
    formsets = []
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_object = self.save_form(request, form, change=False)
            form_validated = True
        else:
            form_validated = False
            new_object = self.model()
        prefixes = {}
        for FormSet, inline in zip(self.get_formsets(request), self.inline_instances):
            prefix = FormSet.get_default_prefix()
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
            if prefixes[prefix] != 1 or not prefix:
                prefix = "%s-%s" % (prefix, prefixes[prefix])
            formset = FormSet(data=request.POST, files=request.FILES,
                              instance=new_object,
                              save_as_new="_saveasnew" in request.POST,
                              prefix=prefix, queryset=inline.queryset(request))
            formsets.append(formset)
        if all_valid(formsets) and form_validated:
            self.save_model(request, new_object, form, change=False)
            form.save_m2m()
            for formset in formsets:
                self.save_formset(request, form, formset, change=False)

            self.log_addition(request, new_object)
            return self.response_add(request, new_object)
    else:
        # Prepare the dict of initial data from the request.
        # We have to special-case M2Ms as a list of comma-separated PKs.
        initial = dict(request.GET.items())
        for k in initial:
            try:'''
ModelForm = self.get_form(request)
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        #可以获取request参数
        # print form.request
        if form.is_valid():
            pass
        else:
            pass
    else:''
        #'''...（计算initial）'''
        form = ModelForm(initial=initial)
复制代码
分析：form = ModelFormMetaClass(request.POST, request.FILES)，按照通常的理解右边应该返回的是ModelFormMetaClass的一个实例，由于重写了__new__函数，没有调用父类函数，而是直接返回了一个带有request参数的MyForm实例，然后调用__init__函数，因此最后ModelFormMetaClass（）返回也是这个实例，而左边也需要的是MyForm的实例对象。因此__new__函数的作用是创建一个实例。
例子：

复制代码
class A(object):
    def __init__(self):
        pass
print type(A)

结果：
<type 'type'>置对象或者类的基类型，object是所有类继承的基类，因此int、str、list、tuple等等这些内置的类，这些都是type类的实例对象。因为type也是类，因此type的基类也是object
#废__new__的写法
class person(object):
    def __new__(cls,*args, **kwargs):
        obj=object.__new__(cls)#super().__new__(cls)+1
        return obj #返回的是一个实例对象，__init__才有机会被调用
        
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def name(self):
        return self.name
p1=person('zhangsan',18)
print (p1.name)
p2=person(p1)
