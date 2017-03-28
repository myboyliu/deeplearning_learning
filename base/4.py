#4.py
# -*- coding: utf-8 -*-
list = ['a','b',10]
print(list);
print(len(list))
print(list[-1])
print(list[-2])
#尾部增加
list.append(20)
print(list)
##插入
list.insert(1,'a1')
print(list)
## 删除
list.pop();
print(list)

## 删除
list.pop(0);
print(list)
## 删除
list.pop(-1);
print(list)

## 替换
list[0]='aa';
print(list)

##不可变数组,只有1个元素的tuple定义时必须加一个逗号,
tuple=('a','b')
print(tuple);



