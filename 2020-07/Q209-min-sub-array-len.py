# -*- coding:utf-8 -*-
# @Time : 2020/7/7 22:35 
# @Author : bendan50
# @File : Q209-min-sub-array-len.py 
# @Function ： 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的子数组，
# 并返回其长度。如果不存在符合条件的子数组，返回 0。
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 输入 s = 213    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
# 输出 8
# 解释：子数组[83, 4, 25, 26, 25, 2, 25, 25]是该条件下长度最小的子数组
# @Software: PyCharm

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        """
        思路：注意子数组的定义，因此不能排序！
        暴力法：从第一个结点开始，往后累加，满足大于等于s后，记录长度，然后继续从第二个结点开始。
            循环到数组尾，时间复杂度O(n^2)
        改进：前后两个指针构建的滑动窗口。sum=nums[head]+...+nums[tail]，个数为tail-head+1
        :param s:
        :param nums:
        :return:
        """
        #第一步：一直往里加（头结点不变，尾结点往后移），直到满足大于等于s，
        head = tail = 0
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        sum = 0
        ret = nums_len + 1      #子数组的长度，因为寻找最小长度，所以比数组长度大1，当结束时，小于等于数组长度说明有解。
        while tail < nums_len:
            if nums[tail] >= s:
                return 1
            sum += nums[tail]
            if sum >= s:
                #后移前指针
                while sum >= s and head <= tail:
                    sum -= nums[head]
                    head += 1
                ret = min(ret,tail-head+2)  # +2是因为tail-head之间应该+1，但此时sum<s了，刚才的头节点应该算上，所以+2
            pass
            tail += 1
        if ret <= nums_len:
            return ret
        else:
            return 0


if __name__ == "__main__":
    s = 213
    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    # s = 7
    # nums = [2, 3, 1, 2, 4, 3]
    ret = Solution().minSubArrayLen(s,nums)
    print(ret)