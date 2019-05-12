import pysnooper


@pysnooper.snoop()
def main():
    """
    __get__：用于访问属性。它返回属性的值，若属性不存在、不合法等都可以抛出对应的异常。
    __set__：将在属性分配操作中调用。不会返回任何内容。
    __delete__：控制删除操作。不会返回内容。
    """

    class Score:
        def __init__(self, default=0):
            self._score = default

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError('Score must be integer')
            if not 0 <= value <= 100:
                raise ValueError('Valid value must be in [0, 100]')

            self._score = value

        def __get__(self, instance, owner):
            return self._score

        def __del__(self):
            del self._score

    class Student:
        math = Score(0)
        chinese = Score(0)
        english = Score(0)

        def __init__(self, name, math, chinese, english):
            self.name = name
            self.math = math
            self.chinese = chinese
            self.english = english

        def __repr__(self):
            return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )

    Student(name='xiaorui', math=100, chinese=22, english=33)

    # __get__中,instance表示实例  owner表示类
    # __set__中,instance表示实例,value表示我们给类属性的值
    """
    如果class定义了它，则这个class就可以称为descriptor。
    owner是所有者的类，instance是访问descriptor的实例，
    如果不是通过实例访问，而是通过类访问的话，instance则为None。
    （descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，
    只有descriptor作为其它类的属性才有意义。）

    可以看出，每次通过实例访问属性，
    都会经过__getattribute__函数。而当属性不存在时，
    仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。
    每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。

    需要注意的是，当使用类访问不存在的变量是，
    不会经过__getattr__函数。而descriptor不存在此问题，
    只是把instance标识为none而已。
    """

    class Integer(object):
        def __init__(self, value):
            self.value = value

        def __get__(self, instance, owner):
            if instance is None:  # 通过类访问
                return self
            else:
                return instance.__dict__[self.value]  # 通过实例访问

        def __set__(self, instance, value):

            if not isinstance(value, int):
                raise TypeError('except a int ')
            instance.__dict__[self.value] = value

        def __delete__(self, instance):
            del instance.__dict__[self.value]

    class Point(object):
        x = Integer('x')  # 实例访问
        y = Integer('y')

        def __init__(self, x, y):
            self.x = x
            self.y = y

    # p = Point(1, 2)
    # p = Point('str', 2)
    # print(p.x)
    # print(p.y)

    class Point2(object):
        def __init__(self, x, y):
            self.x = Integer('x')  # 通过类访问
            self.y = Integer('y')
            self.x = x
            self.y = y

    # p2 = Point2('str2', 5)  # 直接返回的是类本身的init里面的属性 ?
    # print(p2.x)


if __name__ == '__main__':
    main()
