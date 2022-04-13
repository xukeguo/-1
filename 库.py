list_mame=['Waiwu','Lisi','Wangwu','Zhaoliu','Zhangsan']
for i in range(0,len(list_mame)):
    if 'hao' in list_mame[i]:
        print(list_mame[i],i)
for x in list_mame:    
 if 'Waiw' in x:
  print (x.index)
list_age=[18,19,20,21,22]
list_score=[90,80,70,60,50]
for i in range(0,len(list_mame)):
    print('姓名：',list_mame[i],'年龄：',list_age[i],'成绩：',list_score[i])
# for i in range(len(list_mame)):
dict1={x:[y,z] for x,y,z in zip(list_mame,list_age,list_score)}
list1=dict1['Waiwu']
print(dict1)
a=0
for i in range(len(list_mame)):
    for x,y in dict1.items():
      if y[1]>=110:
        print(x,'优秀')
        print(dict1['Lisi'])
        a=1
        break
    else:pass
 
if a!=1:
    print('还没有这么优秀的')
  
#     嵌套if-else
