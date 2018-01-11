# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 上午11:12
# @Author  : Tomcj
# @File    : Roman_to_Integer.py
# @Software: PyCharm

def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result=0

    if len(s)==1:
        return  roman[s]
    else:

        for x in range(len(s)-1):
            if x==0 and roman[s[x]]<roman[s[x+1]]:
                result-=roman[s[x]]

            elif roman[s[x]]<roman[s[x-1]] and roman[s[x]]<roman[s[x+1]]:
                result-=roman[s[x]]
            else:
                result+=roman[s[x]]
        result+=roman[s[-1]]
    return  result
if __name__ == '__main__':

    print romanToInt('MCDXXXVII')