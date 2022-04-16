#我的列表类
from multiprocessing.sharedctypes import Value


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
