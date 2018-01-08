# list
persons = ['laosan', 'laosi', 'laowu']

# append,insert添加 pop删除
# persons.append('laoliu')
# print(persons)
# print(len(persons))
# print(persons[-3])

# 直接赋值
# persons[0] = 'laosana'

# print(persons)

# python 无泛型
# list = ['laosan', 123, True]
# # list 可以包含list  相当于二维数组
# list1 = ['laosan', 123, ['1', '2'], True]
# print(list1[2][1])
# print(list)

# tuple  区别与list   tuple是有序的，声明后不可修改。
# tuple = ('laosan', 'laosi', 'laowu')
#
# print(tuple)

# tuple 的指向不变，但是tuple中的list可变 如：
t = (1, 2, 3, [4, 5])
print(t)
t[3][0] = 6
t[3][1] = 7
print(t)


