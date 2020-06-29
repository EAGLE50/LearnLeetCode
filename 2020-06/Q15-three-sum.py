# -*- coding:utf-8 -*-
# @Time : 2020/6/28 21:53 
# @Author : bendan50
# @File : Q15-three-sum.py 
# @Function ： 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# @Software: PyCharm

class Solution:
    def three_sum(self, nums):
        """
        官方思路，时间最优
        :param nums:
        :return:
        """
        nums.sort()
        nums_len = len(nums)
        ret = list()
        a = 0
        b = 1
        c = nums_len - 1
        while a <= c and b <= c and nums[a] <= 0 and nums[c] >= 0:
            if a >= 1 and nums[a - 1] == nums[a]:
                a += 1
                b = a + 1
                continue
            while b < c:
                if b >= a + 2 and nums[b - 1] == nums[b]:
                    b += 1
                    continue
                sum = nums[a] + nums[b] + nums[c]
                if sum == 0:
                    ret.append([nums[a], nums[b], nums[c]])
                    b += 1
                elif sum > 0:
                    c -= 1
                else:
                    b += 1
            pass
            a += 1
            b = a + 1
            c = nums_len - 1
        return ret

    def threeSum(self, nums):
        """
        暴力法是O(n^3)，所以目标是O(n^2)
        思路：先排序，分出正负数区间；双指针移动，
        结果：超时。
        继续优化：因为不重复，所以当指针移动后，若与上一个数相同，则不需要循环，直接再移动，直到找到不同于上一个数的数
        实现见上方three_sum()方法
        :param nums:
        :return:
        """
        nums.sort()
        nums_len = len(nums)
        ret = list()
        a = 0
        b = 1
        c = nums_len - 1
        while a <= c and b <= c and nums[a] <= 0 and nums[c] >= 0:
            # 下面的循环就是Q1:两数之和+Q11：盛最多水的容器的思路，O(n)的复杂度，计算两个数之和
            while b < c:
                aa = nums[a]
                bb = nums[b]
                cc = nums[c]
                sum = aa + bb + cc
                if sum == 0:
                    if not ret.__contains__(list([aa, bb, cc])):
                        ret.append(list([aa, bb, cc]))
                    b += 1  # 或者 c -= 1 都可以，即任意移动一侧下标指针
                elif sum > 0:
                    c -= 1
                else:
                    b += 1
            pass
            a += 1
            b = a + 1
            c = nums_len - 1
        return ret


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0,0,0]
    # nums = [-1,0,1]
    nums = [-1, 0, 1, 2, -1, -4]  # 考虑去重
    # nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    # nums = [1, 1, -2]
    ret = Solution().threeSum(nums)
    ret2 = Solution().three_sum(nums)
    print(ret)
    print(ret2)
