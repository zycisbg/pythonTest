# -*- coding: utf-8 -*-
# # print('hello,world')
# name = input('please input your name');
# print(name)
# print('1024*768=',1024*768)
# print('张益诚');

# 占位符 %s 字符串 %d 整数 %f 浮点

# print('hello,%s'%'laosan')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# 02d  : 整数占两个位置
# print('%02d--%2d' % (1, 3))

# 推荐用 %s  转义%  需要用%%
# print('%.2f' % 3.1452323)

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 - s1) / s2

print('%.1f' % r)

# format 函数
print('hello,{0},成绩提高了{1:.1f}'.format('老三', 123.243443))
