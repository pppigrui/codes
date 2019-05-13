import pysnooper


@pysnooper.snoop('result.txt', depth=2)
def main():
    class Structure:
        # Class variable that specifies expected fields
        _fields = []

        def __init__(self, *args, **kwargs):
            if len(args) != len(self._fields):
                raise TypeError(
                    'Expected {} arguments'.format(len(self._fields)))

            # Set the arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

            # Set the additional arguments (if any)
            extra_args = kwargs.keys() - self._fields
            # print(kwargs.keys())  # dict_keys(['date'])
            # print(self._fields)  # ['name', 'shares', 'price']
            # print(extra_args)  # {'date'}
            for name in extra_args:
                setattr(self, name, kwargs.pop(name))

            if kwargs:  # 如果还剩元素代表关键字参数在args里面
                raise TypeError(
                    'Duplicate values for {}'.format(
                        ','.join(kwargs)))

    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    # s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2019')
    # print(s1.__dict__)
    print(s2.__dict__)


if __name__ == '__main__':
    main()
