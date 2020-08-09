# -*- coding:utf-8 -*-
# @Time : 2020/8/8 16:06 
# @Author : bendan50
# @File : Q945-min-increment-for-unique.py 
# @FunctionC : 使数组唯一的最小增量
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
# 返回使 A 中的每个值都是唯一的最少操作次数。
# 示例 1:
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 示例 2:
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 提示：
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# @Software: PyCharm

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        """
        思路：先对数组进行排序，然后开始对有序数组进行遍历。
        当第i值小于等于第i-1值时，需要move操作，次数为A[i-1]-A[i]+1，否则不需要move
        :param A:
        :return:
        """
        A.sort()
        sum = 0
        size = len(A)
        for idx in range(1, size):
            if A[idx] <= A[idx - 1]:
                temp = A[idx]
                A[idx] = A[idx - 1] + 1
                sum = sum + (A[idx] - temp)
        pass
        return sum

    def min_IncrementForUnique(self, A: List[int]) -> int:
        """
        这道题特殊的时间复杂度为O(n)的解法：特殊的原因是告知了A[i]的取值范围。
        首先遍历一遍，记录某数出现的次数count[x]
        当我们找到一个没有出现过的数的时候，将之前某个重复出现的数增加成这个没有出现过的数。
        :param A:
        :return:
        """
        count = {}
        size = len(A)
        #第一次遍历，记录数值出现次数
        for i in range(size):
            num = count.get(A[i])
            if num:
                count.__setitem__(A[i],num+1)
            else:
                count.__setitem__(A[i],1)
        #第二次遍历
        sum = 0
        taken = 0
        for idx in range(80000):
            c = count.get(idx) if count.get(idx) else 0
            if c >= 2:
                taken += c - 1
                sum -= idx * (c - 1)
            elif taken > 0 and c == 0:
                taken -= 1
                sum += idx
        return sum

if __name__ == "__main__":
    A = [3,2,1,2,1,7]
    # ret = Solution().minIncrementForUnique(A)
    ret = Solution().min_IncrementForUnique(A)
    print('ret = {}'.format(ret))
