import copy
import pysnooper


@pysnooper.snoop()  # 用于在终端显示运行过程值得变化(用于调试)
def main():
    a = [1, 2, 3, ['a', 'b']]
    id_a = id(a)  # 4484839176

    b = a
    id_b = id(b)  # 4484839176

    c = copy.copy(a)
    id_c = id(c)  # 4484838344 浅拷贝 可变类型变化跟着变化 如列表[]

    d = copy.deepcopy(a)
    id_d = id(d)  # 4484703240 深拷贝 不管原变量怎么变化都不会改变

    a.append(4)
    a[3].append('c')

    # print(a)  # [1, 2, 3, ['a', 'b', 'c'], 4]
    # print(b)  # [1, 2, 3, ['a', 'b', 'c'], 4]
    # print(c)  # [1, 2, 3, ['a', 'b', 'c']]
    # print(d)  # [1, 2, 3, ['a', 'b']]
"""
运行过程:
22:44:58.592382 call         6 def main():
22:44:58.592581 line         7     a = [1, 2, 3, ['a', 'b']]
New var:....... a = [1, 2, 3, ['a', 'b']]
22:44:58.592665 line         8     id_a = id(a)  # 4484839176
New var:....... id_a = 4409517832
22:44:58.592733 line        10     b = a
New var:....... b = [1, 2, 3, ['a', 'b']]
22:44:58.592814 line        11     id_b = id(b)  # 4484839176
New var:....... id_b = 4409517832
22:44:58.592897 line        13     c = copy.copy(a)
New var:....... c = [1, 2, 3, ['a', 'b']]
22:44:58.593148 line        14     id_c = id(c)  # 4484838344
New var:....... id_c = 4409517000
22:44:58.593363 line        16     d = copy.deepcopy(a)
New var:....... d = [1, 2, 3, ['a', 'b']]
22:44:58.593684 line        17     id_d = id(d)  # 4484703240
New var:....... id_d = 4409377800
22:44:58.593816 line        19     a.append(4)
Modified var:.. a = [1, 2, 3, ['a', 'b'], 4]
Modified var:.. b = [1, 2, 3, ['a', 'b'], 4]
22:44:58.593957 line        20     a[3].append('c')   
Modified var:.. a = [1, 2, 3, ['a', 'b', 'c'], 4]  ##a变化之后bc的变化
Modified var:.. b = [1, 2, 3, ['a', 'b', 'c'], 4]  ##a变化之后bc的变化
Modified var:.. c = [1, 2, 3, ['a', 'b', 'c']]  ##a变化之后bc的变化
22:44:58.594113 return      20     a[3].append('c')
Return value:.. None

"""

if __name__ == '__main__':
    main()
