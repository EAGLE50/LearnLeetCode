# -*- coding:utf-8 -*-
# @Time : 2020/9/6 16:04 
# @Author : bendan50
# @File : Q1005-largest-sum-after-k-negations.py 
# @Function :  K 次取反后最大化的数组和
# 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，
# 然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
# 以这种方式修改数组后，返回数组可能的最大和。
# 示例 1：
# 输入：A = [4,2,3], K = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
# 示例 2：
# 输入：A = [3,-1,0,2], K = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
# 示例 3：
# 输入：A = [2,-3,-1,5,-4], K = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
# 提示：
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
# @Software: PyCharm

from typing import List

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        """
        思路：对A先进行排序，然后全部将负数变成正数，最后若K依然剩余且为奇数，则找到最小的值改变符号。
        :param A:
        :param K:
        :return:
        """
        A.sort()
        idx = 0
        while A[idx] < 0 and K > 0:
            A[idx] = -A[idx]
            K -= 1
            idx += 1
        if K % 2 == 0:      #K=0，则无法调整，直接返回和；若K为非零偶数说明此时A均为正数
            return sum(A)
        else:
            if idx == 0:
                A[idx] = -A[idx]
                return sum(A)
            else:
                min_idx = idx if A[idx] < A[idx - 1] else idx - 1
                A[min_idx] = -A[min_idx]
                return sum(A)