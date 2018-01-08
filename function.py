# help(abs)   绝对值
# s = abs(123)
# print(s)

# list = [1, 2, 3, 4]
# i = max(list)
# print(i)
#
# myMax = max
# i1 = myMax(list)
# print(i1)

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs(-13))


# def my_fun(x):
#     if x > 10:
#         print(x)
#     elif x > 8:
#         print('大于8')
#     else:
#         pass
#
# my_fun(3)

# 默认函数
# def power(x, n=2):
#     return print(x*n)
#
# power(5);

# def my_fun(a, b, c=5, d=3):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# my_fun(62,44,d=10)

# 注意事项

# def my_fun(l=[]):
#     l.append('end')
#     return l
# def my_fun(l = None):
#     if l == None:
#         l = []
#     l.append('end')
#     return l
#
# print(my_fun([1,2]))
# print(my_fun([1,2,3]))
# print(my_fun([4,5]))
#
# print(my_fun())
# print(my_fun())
# print(my_fun())


# 可变函数
# def cala(*numbers):
#     sum = 0
#     for number in numbers:
#         sum = sum + number
#     print(sum)
#
# cala(*[10,20])

# 关键字函数
# def person(name, age, **kv):
#     print(name)
#     print(age)
#     print(kv)
#
# # person('laosan', 18, city = 'beijing')
# person('laosan', 18, **{'city ': 'beijing', 'realname' : 'sange'})

#命名关键字函数

# def person(name, age, *, city, realname):
#     print(name)
#     print(age)
#     print(city)
#     print(realname)

# person('laosan',19,city='beijing',realname = 'sange')
# person('laosan',19)


# 递归
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

print(fact(5))