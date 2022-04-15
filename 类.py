#列表类
class mylist:
    #def __init__(self, value):
       # self.value = value
       # self.next = None
        pass
class mylist(list):
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
    def my_insert(self, index, value):
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
lis=mylist([1,2,3,4,5])
print(lis.my_avg())
lis.append(6)
print(lis.my_av())
print(sum(lis))
print(lis.my_sum())



#!/usr/bin/env python3
# Path: 类.py
#数据类型

class myint:
    
    pass
class myint(int):
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
        for i in range(2,self):
              for j in range(2,b):
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
a=myint(55)
print(type(a))
print(a.my_zysfj())
