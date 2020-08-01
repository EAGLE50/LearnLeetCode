# -*- coding:utf-8 -*-
# @Time : 2020/8/1 11:33 
# @Author : bendan50
# @File : Q54-spiral-order.py 
# @Function : 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# @Software: PyCharm

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        思路：就是模拟这个顺时针操作，是一个类似迭代的过程。
        去皮：先左，再下，再右，后上。
        然后更新m,n。 m -= 2; n -= 2
        当m>0 and n>0继续执行去皮
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        ret = list()
        row = len(matrix)  # 行数
        col = len(matrix[0])  # 列数
        r_area = [0, row - 1]  # 遍历时下标的取值范围
        c_area = [0, col - 1]
        size = row * col
        while r_area[0] <= r_area[1] and c_area[0] <= c_area[1] and len(ret) < size:
            r_idx = r_area[0]
            c_idx = c_area[0]
            while c_idx <= c_area[1]:
                ret.append(matrix[r_idx][c_idx])
                c_idx += 1
            c_idx -= 1
            r_idx += 1
            if len(ret) == size:
                break
            while r_idx <= r_area[1]:
                ret.append(matrix[r_idx][c_idx])
                r_idx += 1
            r_idx -= 1
            c_idx -= 1
            if len(ret) == size:
                break
            while c_idx >= c_area[0]:
                ret.append(matrix[r_idx][c_idx])
                c_idx -= 1
            c_idx += 1
            r_idx -= 1
            if len(ret) == size:
                break
            while r_idx > r_area[0]:
                ret.append(matrix[r_idx][c_idx])
                r_idx -= 1
            r_idx += 1
            # 更新区域
            r_area[0] += 1
            r_area[1] -= 1
            c_area[0] += 1
            c_area[1] -= 1
        return ret


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ret = Solution().spiralOrder(matrix)
    print('ret = {}'.format(ret))
