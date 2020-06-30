# -*- coding:utf-8 -*-
# @Time : 2020/6/29 22:57 
# @Author : bendan50
# @File : Q16-three-sum-closest.py 
# @Function：最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# @Software: PyCharm

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        """
        思路：同Q15：三数之和，时间复杂度O(n^2)
        :param nums:
        :param target:
        :return:
        """
        nums_len = len(nums)
        nums.sort()
        a = 0
        b = 1
        c = nums_len - 1
        ret = nums[a] + nums[b] + nums[c] - target
        while a <= c and b <= c:
            if a >= 1 and nums[a - 1] == nums[a]:
                a += 1
                b = a + 1
                continue
            pass
            while b < c:
                if b >= a + 2 and nums[b - 1] == nums[b]:
                    b += 1
                    continue
                val = nums[a] + nums[b] + nums[c] - target
                # val表示与目标的差值，应该趋于0
                ret = val if abs(val) < abs(ret) else ret
                if val == 0:
                    return ret + target
                elif val > 0:
                    c -= 1
                else:
                    b += 1
            a += 1
            b = a + 1
            c = nums_len - 1
        pass
        return ret + target


if __name__ == "__main__":
    ret = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print(ret)
