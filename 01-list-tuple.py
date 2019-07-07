# -*- coding: UTF-8 -*-

# author by : （学员ID)
import random
list1=['blue', 'rabbit']
pos = 0
value = list1[pos]
print('取出列表第%d个值，它是%s'%(pos,value))

print('---输出列表所有元素')
pos = 0
for v in list1:
    print('取出列表第%d个值，它是%s'%(pos,v))
    pos=pos+1

newvalue = 'white'
list1[0] = newvalue
print('---输出更新后的列表中所有元素')
pos = 0
for v in list1:
    print('取出列表的第%d个值，它是%s'%(pos,v))
    pos=pos+1

for i in range(1,5):
    s = random.choice(list1)
    print(s)
