# -*- coding:utf-8 -*-
# @Time : 2020/9/9 20:05 
# @Author : bendan50
# @File : Q376-wiggle-max-length.py 
# @Function : 摆动序列
# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。
# 少于两个元素的序列也是摆动序列。
# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
# 相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。
# 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
# 示例 1:
# 输入: [1,7,4,9,2,5]
# 输出: 6
# 解释: 整个序列均为摆动序列。
# 示例 2:
# 输入: [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
# 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
# 示例 3:
# 输入: [1,2,3,4,5,6,7,8,9]
# 输出: 2
# 进阶:
# 你能否用 O(n) 时间复杂度完成此题?
# @Software: PyCharm

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        思路：类似于【Q122：买卖股票的最佳时机 II】采用峰谷法，即贪心算法的策略
        序列由峰、谷两个端点的值组成，必定是来回摆动的。
        是上升还是下降？diff = nums[i]-nums[i-1]; 如果diff>0，则是上升；如果diff<0，则是下降。
        如何判断是峰或谷呢？diff<0时，num[i+1]-nums[i]>0
        :param nums:
        :return:
        """
        size = len(nums)
        if size < 2:
            return size
        count = 2 if nums[0] != nums[1] else 1  #只要数组长度不小于2，且前两个数不相同，最小值就是2个元素
        prediff = nums[1] - nums[0]
        for i in range(2,size):     #从第三个数开始
            diff = nums[i]-nums[i-1]
            if (prediff <= 0 and diff >0) or (prediff>=0 and diff<0):
                count +=1
                prediff = diff  #只有更新计数时才改变方向。因为diff和prediff总要保持异号
        return count


if __name__ == "__main__":
    # nums = [1,2,3,4,5,6,7,8,9]
    nums = [1,17,5,10,13,15,10,5,16,8]
    ret = Solution().wiggleMaxLength(nums)
    print(ret)
