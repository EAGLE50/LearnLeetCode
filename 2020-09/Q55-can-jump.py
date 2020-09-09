# -*- coding:utf-8 -*-
# @Time : 2020/9/6 22:48 
# @Author : bendan50
# @File : Q55-can-jump.py 
# @Function : 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 示例 2:
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# @Software: PyCharm
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：首先是什么原因会造成到达不了最后一个位置？
        就是无论如何走，都会到达一个点，即必定经过一个点，而这个点的最大踊跃值恰巧是0
        问题进而变成了，从头开始遍历，找到一个0后就扪心自问，从起始位置开始跳跃，这个0是不是必定经过的！
        若是必定经过的，且不是最后一个位置，则永远无法到达最后一个位置。
        若不是必定经过的，则更新起始位置，继续寻找下一个0
        还剩一个问题：如何判断一个位置是不是必定经过的？
        发现又回来了！！！
        参见官方思路后，整理如下：
        贪心算法思想，维护一个最远可到达的值，不断更新。当最远可到达的值大于等于最后一个位置时，则说明肯定能到达。
        :param nums:
        :return:
        """
        max_idx = 0
        last_idx = len(nums) - 1
        for idx,ele in enumerate(nums):
            if idx > max_idx:
                return False
            max_idx = max(max_idx,idx+ele)
            if max_idx >= last_idx:
                return True
        return max_idx >= last_idx

if __name__ == "__main__":
    # nums = [3,0,0,0]
    # nums = [1,1,0,1]
    nums = [2,0,2,0,1]
    ret = Solution().canJump(nums)
    print('ret = {}'.format(ret))

