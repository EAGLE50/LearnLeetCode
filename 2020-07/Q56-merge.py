# -*- coding:utf-8 -*-
# @Time : 2020/7/12 17:13 
# @Author : bendan50
# @File : Q56-merge.py 
# @Function : 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# @Software: PyCharm
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        思路：感觉要两两比较，所以时间复杂度为O(n^2)，非官方，未看解析。
        新列表new[]，取出old[]列表里的一个元素，查看是否与new[]中的元素可以合并
        若可以合并，是合并，更新new[]；若不可以合并，则添加到new[]中，当old[]为空时，退出，返回new[]
        不对！若合并了，可能导致之前不能合并的现在又可以合并了，难道还得再循环吗？
        改进：如果先对old[]进行排序呢？这样就不会存在合并了，导致之前不能合并的现在又能合并的问题了。
        该方法尝试一下，而且时间复杂度为O(nlogn)+O(n)=O(nlogn),即为排序的时间复杂度
        :param intervals:
        :return:
        """
        inter_num = len(intervals)
        if inter_num == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        for i, ele in enumerate(intervals):
            ret_size = len(ret)
            last = ret[ret_size - 1]    #只需要取最后一个元素即可
            merge_ele = self.util(last, ele)
            if len(merge_ele) != 0:
                ret.pop(ret_size - 1)
                ret.append(merge_ele)
            else:
                ret.append(ele)
        return ret

    def util(self, a, b):
        min_idx = min(a[0], b[0])
        max_idx = max(a[1], b[1])
        if a[0] <= b[0] and a[1] >= b[0]:
            return [min_idx, max_idx]
        elif b[0] <= a[0] and b[1] >= a[0]:
            return [min_idx, max_idx]
        else:
            return []

if __name__ == "__main__":
    intervals = [[1,4],[0,0]]
    ret = Solution().merge(intervals)
    print('ret = {}'.format(ret))