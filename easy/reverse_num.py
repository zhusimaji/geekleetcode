# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午4:58
# @Author  : Tomcj
# @File    : reverse_num.py
# @Software: PyCharm

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = cmp(x, 0)
    r = int(`s * x`[::-1])
    return s * r * (r < 2 ** 31)



if __name__ == '__main__':
    print reverse(123)