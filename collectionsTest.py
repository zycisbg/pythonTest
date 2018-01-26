#  相当于集合的包装类
from collections import namedtuple, deque, defaultdict, OrderedDict


Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)

print(p.y)

q = deque(['1', '2', '3'])

q.append('4')

print(q)

# defaultdict   如果有key值返回key值  如果没有key值 返回指定的

dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# orderedDict  有序的 dict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

