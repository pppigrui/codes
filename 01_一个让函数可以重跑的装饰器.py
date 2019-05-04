from functools import wraps
from time import sleep


class Retry(object):
    """
    类装饰器
    """

    def __init__(self, times=2, wait=0, errors=(Exception,)):
        self.times = times
        self.wait = wait
        self.errors = errors

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(1, self.times + 1):
                try:
                    print("retry {} times ".format(_))
                    return func(*args, **kwargs)
                except self.errors:
                    sleep(self.wait)

        return wrapper


def retry(times=2, wait=2, errors=(Exception,)):
    """
    带参数的装饰器
    :param times:重跑次数
    :param wait: 等待时间
    :param errors: 异常
    :return:
    """

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(1, times + 1):
                try:
                    print("retry {} times ".format(_))
                    return func(*args, **kwargs)
                except errors:
                    sleep(wait)
        return wrapper
    return decorate


@retry(times=3)
# @Retry(times=3)
def test():
    raise TypeError('xxxx')


test()
