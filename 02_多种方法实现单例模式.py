import threading

from functools import wraps


# 装饰器实现单例模式
def singleton(cls):
    """
    装饰器实现单例
    :param cls: 类
    :return:
    """
    lock = threading.Lock()  # 加了一把锁,防止资源竞争
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with lock:
                instance[cls] = cls(*args, **kwargs)

        return instance[cls]

    return wrapper


@singleton
class People(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


p1 = People('xiaorui')
p2 = People('xiaoming')
print(p1)
print(p2)
print(p1 is p2)

print('*' * 20)


# 元类实现单例
class SingletonMeta(type):

    def __init__(cls, *args, **kwargs):
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            with cls.lock:
                cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class People2(metaclass=SingletonMeta):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


p3 = People2('xiaorui')
p4 = People2('xiaoming')
print(p3)
print(p4)
print(p3 is p4)
print('*' * 20)


class SingletonPeople:
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            with cls.lock:
                cls.instance = super(SingletonPeople, cls).__new__(cls)
        return cls.instance


class People3(SingletonPeople):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


p5 = People3('xiaorui')
p6 = People3('xiaoming')
print(p5)
print(p6)
print(p5 is p6)
print('*' * 20)

# 使用模块来创建单例
from singleton import people

print(people)
"""
其实，Python 的模块就是天然的单例模式，
因为模块在第一次导入时，会生成 .pyc 文件，
当第二次导入时，就会直接加载 .pyc 文件，
而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，
就可以获得一个单例对象了。
"""
