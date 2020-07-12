# -*- coding:utf-8 -*-
# @Time : 2020/7/12 22:25 
# @Author : bendan50
# @File : Q35-search-insert.py 
# @Function : 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，
# 返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。
# 输入: [1,3,5,6], 5
# 输出: 2
# 输入: [1,3,5,6], 2
# 输出: 1
# 输入: [1,3,5,6], 7
# 输出: 4
# 输入: [1,3,5,6], 0
# 输出: 0
# @Software: PyCharm

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        思路：既然nums是一个排序的数组，它就是不想让从头遍历，时间复杂度为O(n)，而是使用二分法查看
        :param nums:
        :param target:
        :return:
        """
        size = len(nums)
        if size == 0:
            return 0
        head = 0
        tail = size - 1
        while head <= tail :
            mid = (head + tail)//2
            if nums[mid]==target:
                return mid
            if nums[mid] < target:
                head = mid+1
            else:
                tail = mid-1
        return head

if __name__ =="__main__":
    nums =[1,3,5,6]
    target = 7
    ret = Solution().searchInsert(nums,target)
    print('ret = {}'.format(ret))