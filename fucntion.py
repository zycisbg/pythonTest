from functools import reduce, partial


def add(x, y, f):
    return f(x) + f(y)


print(add(-3, -4, abs))

# map 函数相当于是循环调用
it = map(abs, [-1, -3, -4])
print(list(it))


# reduce 函数相当于是 利滚利
def pingfang(x, y):
    return x * y


print(reduce(pingfang, [3, 5, 6]))

# filter  过滤


# sorted 排序

print(sorted([1, 5, 2, 66, -33]))
print(sorted([1, 5, 2, 66, -33], key=abs, reverse=True))


# 返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax

    return sum


f = lazy_sum(1, 5, 6)
print(f)
print(f())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
print(f1())


def count1():
    fs = []
    def f(x):
        def g():
            return x * x
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

q1, q2, q3 = count1()

print(q2())


# lambda
s = map(lambda x: x * x, [1, 3, 6, 7])
print(list(s))


# 装饰器 decorator



def log(func):
    def wapper(*args , **kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wapper

@log
def now():
    print('2018-01-10')

now()


# 偏函数 partial
int2 = partial(int, base=2)

print(int2('10000'))