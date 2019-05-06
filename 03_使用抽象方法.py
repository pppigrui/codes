from abc import ABCMeta
from abc import abstractmethod

"""
苹果每斤4块,
香蕉5块起卖,多一斤1块钱,
西瓜10块钱一个,

"""


# 抽象类不可以直接实例化,只能被继承,继承的类必须实现被abstractmethod修饰的方法
class FruitBase(metaclass=ABCMeta):
    """水果基类"""

    def __init__(self, kind):
        self.kind = kind  # 水果种类

    @abstractmethod
    def get_money(self):
        """水果卖多少钱的规则"""
        pass


class Apple(FruitBase):
    """
    苹果类
    jin:代表多少斤
    """

    def __init__(self, kind, jin):
        super().__init__(kind)
        self.jin = jin

    def get_money(self):
        return 4 * self.jin


class Watermelon(FruitBase):
    """
    西瓜类
    """

    def get_money(self):
        return 10


class Banana(FruitBase):
    """
    香蕉类
    jin:代表格外买了多少斤,默认为0
    """

    def __init__(self, kind, jin=0):
        super().__init__(kind)
        self.jin = jin

    def get_money(self):
        return 5 + 1 * self.jin


class Factory:
    """
    创建水果类实例的工厂(工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合)
    """

    @staticmethod  # 静态方法,类和实例都可以调用
    def create_fruit(types, *args, **kwargs):
        if types == 'banana':
            fruit = Banana(*args, **kwargs)
        elif types == 'watermelon':
            fruit = Watermelon(*args, **kwargs)
        elif types == 'apple':
            fruit = Apple(*args, **kwargs)
        return fruit


def main():
    fruits = [
        Factory.create_fruit('banana', '香蕉', 2),
        Factory.create_fruit('watermelon', '西瓜'),
        Factory.create_fruit('apple', '苹果', 10)
    ]
    for fruit in fruits:
        print('{0}卖了{1}元'.format(fruit.kind, fruit.get_money()))


if __name__ == '__main__':
    main()
