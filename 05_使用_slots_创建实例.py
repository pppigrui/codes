class People(object):
    """
    使用_slots_可以极大的减少创建实例是内存的开销
    某个类要创建大量实例的时候可以用这个方法
    类的属性只能是_slots_里面的 只能少 不能多
    """
    __slots__ = ['name', 'age', 'tel']

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


p = People('xiaorui', 23, 181)
# p.__dict__ 使用_slots_创建的实例没有__dict__方法
