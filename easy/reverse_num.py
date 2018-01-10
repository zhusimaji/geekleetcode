# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午4:58
# @Author  : Tomcj
# @File    : reverse_num.py
# @Software: PyCharm

# leetcode认定所有负数都不是回文，所以需要加上这个判定
# 其实类似的-212负数抛弃掉符号都是回文，定义规则不一样而已
def isPlindrome(x):

    if x<0:
        return  False
    s = cmp(x, 0)
    r = int(`s * x`[::-1])
    return s * r * (r < 2 ** 31)==x
