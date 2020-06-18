# -*- coding:utf-8 -*-
# @Time : 2020/6/17 20:25 
# @Author : bendan50
# @File : Q1-two-sum.py 
# @Function 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# @Software: PyCharm

class Solution:
    """
    思路：暴力，O(n^2)的复杂度肯定不是想要的。要向O(n)靠近。
    第一点：给出数组中的一个值，就能知道它所在的下标，复杂度O(1)，则需要hash，构建字典。key为值，value为下标。
    第二点：构建字典，需遍历一次。若字典中已经存在target-key的键值，说明找到了。即边构建字典边查找。
    """
    def two_sum(self, nums, target):
        idx_hash = {}
        for idx, value in enumerate(nums):
            if idx_hash.keys().__contains__(target - value):
                return [idx_hash.get(target - value), idx]
            idx_hash.__setitem__(value, idx)
        return []


if __name__ == '__main__':
    eagle = Solution()
    # ret = eagle.twoSum([7, 2, 11, 15], 9)
    # ret = eagle.twoSum([3, 2, 4], 6)
    # ret = eagle.twoSum([3, 3], 6)
    # ret = eagle.twoSum([-10, 7, 19, 15], 9)
    ret = eagle.two_sum([-10, 7, 19, 15], 9)
    ret = eagle.two_sum([-10, 7, 19, 15], 9)
    ret = eagle.two_sum([-10, 7, 19, 15], 9)
    ret = eagle.two_sum([-10, 7, 19, 15], 9)
    print('ret = {}'.format(ret))
