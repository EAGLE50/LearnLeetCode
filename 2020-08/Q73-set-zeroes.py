# -*- coding:utf-8 -*-
# @Time : 2020/8/1 17:54 
# @Author : bendan50
# @File : Q73-set-zeroes.py 
# @Function : 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
# @Software: PyCharm

from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        简单方案O(m+n)的额外空间，记录哪行哪列有零
        """
        raw = set()
        col = set()  # 集合，保证唯一性
        r_size = len(matrix)
        c_size = len(matrix[0])
        for i, raw_list in enumerate(matrix):
            for j, ele in enumerate(raw_list):
                if ele == 0:
                    raw.add(i)
                    col.add(j)
        # 按行按列置零数组
        for r in raw:
            for idx in range(c_size):
                matrix[r][idx] = 0
        for c in col:
            for idx in range(r_size):
                matrix[idx][c] = 0
        pass
        # 打印下
        print('matrix = {}'.format(matrix))

    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        思路：进阶，使用O(1)的空间复杂度。
        利用数组本身的存储空间，当matrix[i][j]==0时
        matrix[i][0] = 0
        matrix[0][j] = 0
        这样一来，根据首行首列即可置零
        注：比较特殊的是matrix[0][0]这个位置，当它等于0时，是表示行置零呢还是列置零呢？
        所以需要一个额外的空间记录下。
        flag = False，表示列需要置零
        matrix[0][0]依然表示行需要置零
        :param matrix:
        :return:
        """
        flag = False     #首行是零时，不能更新首行
        for i,raw_list in enumerate(matrix):
            if raw_list[0] == 0:
                flag = True
            for j,ele in enumerate(raw_list):
                if j != 0 and ele == 0:     #关键：j != 0，若j=0,则matrix[0][0]=0,而应该是对flag赋值True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        pass
        r_size = len(matrix)
        c_size = len(matrix[0])
        for raw in range(1,r_size):
            for col in range(1,c_size):
                if matrix[0][col] == 0 or matrix[raw][0] == 0:
                    matrix[raw][col] = 0
        if matrix[0][0] == 0:
            for idx in range(c_size):
                matrix[0][idx] = 0
        if flag:
            for idx in range(r_size):
                matrix[idx][0] = 0
        print(matrix)


if __name__ == "__main__":
    # matrix = [
    #     [0, 1, 2, 0],
    #     [3, 4, 5, 2],
    #     [1, 3, 1, 5]
    # ]
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
    matrix = [[1, 1, 1], [0, 1, 2]]
    # Solution().setZeroes(matrix)
    Solution().set_zeroes(matrix)
