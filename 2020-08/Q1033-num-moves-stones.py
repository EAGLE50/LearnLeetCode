# -*- coding:utf-8 -*-
# @Time : 2020/8/5 19:56 
# @Author : bendan50
# @File : Q1033-num-moves-stones.py
# @Function : 移动石子直到连续
# 三枚石子放置在数轴上，位置分别为 a，b，c。
# 每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，
# 并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
# 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
# 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
# 输入：a = 1, b = 2, c = 5
# 输出：[1, 2]
# 解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
# 输入：a = 4, b = 3, c = 2
# 输出：[0, 0]
# 解释：我们无法进行任何移动。
# @Software: PyCharm

from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        思路：最小值无非是0、1、2，注意区分各种情况；最大值也好算，相当于计算两头点与中间点隔了多少个点
        :param a:
        :param b:
        :param c:
        :return:
        """
        temp = [a,b,c]
        temp.sort()
        a,b,c=temp
        start = b - a - 1
        end = c - b - 1
        if start == 0 or end == 0:      #若一边无法移动，或两边都无法移动，则最小值是0或1
            ret_min = min(start+end,1)
        elif start == 1 or end == 1:    #若一边只能移动一个，那么另一边直接移动到这边的那一个空点上即可。
            ret_min = 1
        else:
            ret_min = 2
        return [ret_min,start+end]
        pass

if __name__ == "__main__":
    a,b,c = [1,3,5]
    ret = Solution().numMovesStones(a,b,c)
    print('ret = {}'.format(ret))
