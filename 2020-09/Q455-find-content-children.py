# -*- coding:utf-8 -*-
# @Time : 2020/9/3 19:13 
# @Author : bendan50
# @File : Q455-find-content-children.py 
# @Function : 分发饼干
# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
# 对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；
# 并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
# 注意：
# 你可以假设胃口值为正。
# 一个小朋友最多只能拥有一块饼干。
# 示例 1:
# 输入: [1,2,3], [1,1]
# 输出: 1
# 解释:
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。
# 示例 2:
# 输入: [1,2], [1,2,3]
# 输出: 2
# 解释:
# 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
# 你拥有的饼干数量和尺寸都足以让所有孩子满足。
# 所以你应该输出2.
# @Software: PyCharm

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        思路：贪心算法，对孩子的胃口从小到大排序，优先满足胃口小的孩子，这样满足的孩子总数才会最多。
        :param g:
        :param s:
        :return:
        """
        if len(s) == 0 or len(g) == 0:
            return 0
        g.sort()
        s.sort()
        ret = 0
        start = 0   # 饼干开始的下标
        for _,i in enumerate(g):
            while start < len(s) and  i > s[start]:     #注意边界安全
                start += 1
            if start >= len(s):
                break
            if i <= s[start]:
                ret += 1
                start += 1
        return ret
