class Dog:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            print('不是实例访问')
            return self
        print('是实例访问')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if instance is None:
            print('bushishili')
            raise TypeError('xxxx')
        print('shishili')
        instance.__dict__[self.name] = value

    def __repr__(self):
        return self.name


class People:
    d = Dog('xiaohei')

    def __init__(self):
        self.d1 = Dog('xix')


p = People()
print(People.d)
