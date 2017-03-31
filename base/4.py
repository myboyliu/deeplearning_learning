# 4.py
# -*- coding: utf-8 -*-
list = ['a', 'b', 'd','c']
print(list)
list.sort()
print(list)
print(len(list))
print(list[-1])
print(list[-2])
# 尾部增加
list.append(20)
print(list)
# 插入
list.insert(1, 'a1')
print(list)
# 删除
list.pop()
print(list)

# 删除
list.pop(0)
print(list)
# 删除
list.pop(-1)
print(list)

# 替换
list[0]='aa'
print(list)

# 不可变数组,只有1个元素的tuple定义时必须加一个逗号,
tuple=('a', 'b')
print(tuple)

dict = {"a": 1, "b": 2}
print(dict)
print(dict['a'])

print('a' in dict)
print('c' in dict)

print(dict.get('a'))

print(dict.get('c', 2))

print(dict.pop('a'))
print(dict)


s = set(['b', 1, 1, 2, 3,'a'])
s.add(5)
print(s)
s.remove(5)
print(s)
s2 = set([3, 4, 5])
print(s & s2)


