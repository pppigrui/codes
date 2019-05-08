class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('except a string for name')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("name can't be deleted")

    @property
    def age(self):
        return self._age

    @age.setter  # 这里可以对属性进行判断和各种修改
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('except a int for age')
        self._age = value

    @age.deleter
    def age(self):
        raise AttributeError("age can't be deleted")

    def __repr__(self):
        return "name is {0} and age is {1}".format(self.name, self.age)


# p = People('xiaorui',"23") #TypeError: except a int for age
# del p.name # AttributeError: name can't be deleted
p = People('xiaorui', 23)
