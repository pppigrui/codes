import math

"""
当一个描述器被放入一个类的定义时， 每次访问属性时它的 __get__() 、__set__() 和
`__delete__()` 方法就会被触发
"""
def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(7.9)
print(c.radius)
print(c.area)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)
print(c.perimeter)
