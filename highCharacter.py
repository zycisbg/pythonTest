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

# list = ['a', 'b', 'c', 'd']
# for i,str in enumerate(list):
#     print(i,str)


# 列表生成器
# import os
#
# l = list(range(100))
# print(l)
#
# l = [x * x for x in range(10)]
# print(l)
#
# l = [d for d in os.listdir('c:')]
# print(l)

# d = {'laosan': 18, 'laosi': 19, 'laowu': 33, 'laoliu': 99}
# items = d.items()
# for x, y in items:
#      print(x, ':', y)
# var = [x + ':' + str(y) for x, y in items]
# print(var)

# 生成器
# 列表元素可以按照某种算法推算出来,不用建立完整的list  这种一边循环一边计算的机制就叫做生成器 generator

# l = [x for x in range(20)]
#
# print(l)

# g = (x for x in range(20))
#
# print(g)
# print(next(g))
#
# for x in g:
#     print(x)

# 用函数打印斐波拉契数列
# 斐波拉契数列和 generator 非常相似

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n+1
#     return 'done'
#
# fib(20)

# generator函数
# def odd():
#     yield 1
#     yield 2
#     yield 3
#     return 'done'
#
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))


# for 循环打不出 generator函数 的返回值，只有抓获异常获取返回值

# for item in o:
#     print(item)

# while True:
#     try:
#         print(next(o))
#     except StopIteration as e:
#         print(e.value)
#         break

# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
