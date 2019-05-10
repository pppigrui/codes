import collections

from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import ChainMap
from collections import Sequence
from collections import Counter


# print(collections.__all__)

def test_namedtuple():  # namedtuple('名称', [属性list])
    """
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
    并可以用属性而不是索引来引用tuple的某个元素。

    这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，
    又可以根据属性来引用，使用十分方便。

    可以验证创建的Point对象是tuple的一种子类：
    :return:
    """
    # print(dir(namedtuple))
    Point = namedtuple(typename='Point', field_names=['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(isinstance(p, tuple))
    print(isinstance(p, Point))


def test_deque():
    """
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
    因为list是线性存储，数据量大的时候，插入和删除效率很低。
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
    这样就可以非常高效地往头部添加或删除元素。
    deque有的方法
    'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft',
    'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate']
    :return:
    """
    d = deque([1, 2, 3], maxlen=10)
    # print(dir(deque))
    d.append('append')
    d.appendleft('appendleft')
    # d.clear()
    # d2 = d.copy()
    # print(d2)
    # print(d.count(1))
    # d.extend([4,5,6])
    # d.extendleft([7,8,9])
    print(d)


def test_defaultdict():
    """
    defaultdict(n) n可以为list, tuple, dict str
    当key不存在的时候回对应返回一个空的 list[], tuple(), dict{} str ''

    defaultdict的方法:
    'clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items',
    'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

    如果想自定义默认值的话可以加一个lambda:'默认值'
    :return:
    """
    # print(dir(defaultdict))
    dic1 = defaultdict(lambda: 'key不存在时的默认值')
    dic1['x'] = 1
    dic1['y'] = 2
    print(dic1['x'])
    print(dic1['y'])
    print(dic1['z'])  # 不存在 会打印出默认值


def test_orderdict():
    """
    字典本来是无序的 但是orderdict是有序的
    oredrdict的顺序是按照key插入的书序排的
    Orderdict的方法:
    'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
     'move_to_end', 'pop', 'popitem', 'setdefault', 'update', 'values'
    :return:
    """
    # print(dir(OrderedDict))
    order_dic = OrderedDict()
    order_dic['x'] = 1
    order_dic['z'] = 2
    order_dic['y'] = 3
    print(order_dic)
    print(order_dic.keys())


def test_chainmap():
    """
    合并两个字典: 以前的作坊式dic1.update(dic2) 但是这样
    dic1就变了 如果不想让dic1改变的话可以用到ChainMap

    ChainMap 可以在不修改以前的字典的情况下降两个或者多个字典合并
    :return:
    """
    dic1 = {'x': 1}
    dic2 = {'y': 2}
    new_dic = ChainMap(dic1, dic2)
    print(dic1)
    print(dic2)
    print(new_dic)

def test_counter():
    """
    用于统计 ,一个简单的计数器
    Counter的方法有:
    'clear', 'copy', 'elements', 'fromkeys', 'get', 'items',
     'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values'
    :return:
    """
    # print(dir(Counter))
    s = 'qdafhjakshehfajkfhj'
    result=Counter(s) #统计的记过
    # print(result.most_common(3)) #出现个数最多的三个数
    # print(result.keys())
    # print(result.get('q'))


if __name__ == '__main__':
    test_namedtuple()
    # test_deque()
    # test_defaultdict()
    # test_orderdict()
    # test_chainmap()
    # test_counter()