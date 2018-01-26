# class Student(object):
#     # init 方法相当于是构造器
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# stu = Student('bob', 18)
# print(stu.name)


# 封装

# 加 两个下划线 相当于 用private 修饰
# class Person(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     # getter setter
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#
# per = Person('zhangsan', 18)
# per.set_name('laosi')
# print(per.get_name())

# 类的继承，  父类在（）中


# slots
# from types import MethodType
#
#
# class Student(object):
#     __slots__ = ('name', 'age') #仅对此属性可以在外绑定
#     pass
#
# s = Student();
#
# s.name = 'laosan'
# print(s.name)
#
# def set_name(self,name):
#     self.name = name
#
# # 给实例对象绑定方法。 （动态语言）
# s.set_name = MethodType(set_name,s)
#
# s.set_name('laosi')
# # 给class绑定
# Student.set_name = set_name
#
# print(s.name)

# @property


class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # @property # 方法变为属性
    # def say(self):
    #     return '%s : %s' % (self.__name, self.__age)

    # toString
    def __str__(self):
        return '%s : %s' % (self.__name, self.__age)

per = Person('zhangsan', '18')
print(per)


