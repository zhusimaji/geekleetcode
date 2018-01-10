# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 上午10:00
# @Author  : Tomcj
# @File    : Palindrome_Number.py
# @Software: PyCharm

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = cmp(x, 0)
    r = int(`s * x`[::-1])
    return s * r * (r < 2 ** 31)
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """