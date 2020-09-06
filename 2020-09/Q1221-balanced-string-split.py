# -*- coding:utf-8 -*-
# @Time : 2020/9/6 17:49 
# @Author : bendan50
# @File : Q1221-balanced-string-split.py 
# @Function : 分割平衡字符串
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 返回可以通过分割得到的平衡字符串的最大数量。
# 示例 1：
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
# 示例 2：
# 输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
# 示例 3：
# 输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".
# 提示：
# 1 <= s.length <= 1000
# s[i] = 'L' 或 'R'
# 分割得到的每个字符串都必须是平衡字符串。
# @Software: PyCharm

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        思路：典型的贪心算法，从头开始遍历，记录L和R的个数，当相等时说明可以分割，+1
        :param s:
        :return:
        """
        Ls = []
        Rs = []
        ret = 0
        for _,ele in enumerate(s):
            if ele == 'R':
                Rs.append(ele)
            else:
                Ls.append(ele)
            if len(Ls) == len(Rs):
                ret += 1
                Rs.clear()
                Ls.clear()
        return ret