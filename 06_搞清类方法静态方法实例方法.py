"""
实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。
类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：实例对象和类对象都可以调用。
静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：实例对象和类对象都可以调用。
"""
class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_people(cls, name, age):
        """
        通过类方法创建实例
        :param name:
        :param age:
        :return:
        """
        print('类方法: 只有类可以调用 可以创建实例')
        if not isinstance(name, str):
            raise TypeError('except a string for name')

        if not isinstance(age, int):
            raise TypeError('except a int for age')
        if age < 30:
            return cls(name, age)
        return cls(name, age - 5)

    @staticmethod
    def eat():
        print('静态方法: 类和实例都可以调用')

    def walk(self):
        print('实例方法: 类和类实例可以调用,但是类调用的时候要传一个参数,实例访问不用传参')

    def __repr__(self):
        return 'name is {} and age is {}'.format(self.name, self.age)

p1 = People.create_people('pppigrui', 29)
p2 = People('xiaorui', 23)
People.eat()
People.walk('x')
p2.walk()
