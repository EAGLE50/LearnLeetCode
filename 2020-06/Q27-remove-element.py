# -*- coding:utf-8 -*-
# @Time : 2020/6/24 22:33 
# @Author : bendan50
# @File : Q27-remove-element.py 
# @Function : 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# @Software: PyCharm

class Solution:
    def removeElement(self, nums, val: int) -> int:
        """
        思路：定义两个下标索引，一个从头找val，一个从尾找非val，然后互换。类似快排的处理逻辑
        注：谨防数组越界
        :param nums:
        :param val:
        :return:
        """
        idx_head = 0
        idx_tail = len(nums) - 1
        nums_len = len(nums)
        while idx_head < idx_tail:
            while idx_head < idx_tail and nums[idx_head] != val:
                idx_head += 1
            while idx_tail > idx_head and nums[idx_tail] == val:
                idx_tail -= 1
            # 不能少了关键判断，否则头尾下标会多一次变化。
            if nums[idx_head] == val and nums[idx_tail] != val:
                temp = nums[idx_head]
                nums[idx_head] = nums[idx_tail]
                nums[idx_tail] = temp
                idx_head += 1
                idx_tail -= 1
        # 考虑边界
        # 第一种情况：idx_head = idx_tail
        if idx_head == idx_tail:
            if nums[idx_tail] == val:
                idx_tail -= 1
        return idx_tail + 1

    def remove_element(self, nums, val: int) -> int:
        """
        官方更简捷地实现，思路完全相同，均为双指针法。
        :param nums:
        :param val:
        :return:
        """
        idx = 0
        nums_len = len(nums) - 1
        while idx <= nums_len:
            if nums[idx] == val:
                temp = nums[idx]
                nums[idx]=nums[nums_len]
                nums[nums_len]=temp
                nums_len -= 1
            else:
                idx += 1
        return nums_len+1


if __name__ == '__main__':
    nums = list([3, 3])
    # ret = Solution().removeElement(nums,5)
    ret = Solution().removeElement(nums, 3)
    print('ret = {}'.format(ret))
