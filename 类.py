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
    def my_zysfj(self):
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
    def my_rfloordiv(self, value):
        return value // self
a=Myint(55)
b=5
c=32
c=Myint(c)
print(Myint.my_zysfj(b))
print(a.my_zysfj())
print(Myint(b).my_zysfj())
#print(Myint.my_zysfj(c))
#我的字典类型
class Mydict:
    pass
class Mydict(dict):
    def my_get(self, key):
        return self.get(key)
    def my_set(self, key, value):
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
dic.my_minx()
