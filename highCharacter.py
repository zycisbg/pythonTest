# python 高级特性
# 切片 正数去头

# l = [1, 3, 4, 5, 6, 7]
# print(l[1:3])

# 切片 倒数去尾

# print(l[-3:-1])
# print(l[-3:])
#
# l = list(range(100))
# print(l[:10])
# print(l[::2])

# 迭代
from collections import Iterable

# print(isinstance('abc', Iterable))

list = ['a', 'b', 'c', 'd']
for i,str in enumerate(list):
    print(i,str)


# 列表生成器
