# 5.py
# -*- coding: utf-8 -*-
# 判断
# age=18
# age=30
age = 55

if age < 30:
    print("<30")
elif age == 30:
    print(30)
else:
    print('other')
# x=1
x = []
# x=''
if x:
    print("零数值、or 空字符串 or 非空list")

if not x:
    print("零数值 or 空字符串 or 空list")


# 循环
list = [1, 2, 3, 4, 5]

for num in list:
    print(num)


list = range(10,20)
for num in list:
	print(num)

print('=========')
index=0
while index <= len(list)-1 :
    print(list[index])
    index=index+1

exit()