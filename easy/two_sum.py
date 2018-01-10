# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午3:47
# @Author  : cuijian
# @File    : two_sum.py
# @Software: PyCharm
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = dict()
        for x in range(len(nums)):
            if dict_nums.has_key(target - nums[x]):
                return [dict_nums[target - nums[x]], x]
            dict_nums[nums[x]]=x