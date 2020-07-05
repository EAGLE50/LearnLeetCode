# -*- coding:utf-8 -*-
# @Time : 2020/7/5 10:26 
# @Author : bendan50
# @File : Q14-longest-common-prefix.py 
# @Function :最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# @Software: PyCharm

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        思路：时间复杂度肯定不能低于O(mn)，其中m是公共前缀字符数，n是列表个数。
        分行扫描和列扫描两种。行扫描我最为理解。
        A/B的前缀为pre,那么A/B/C的前缀就等于pre/C的前缀。
        :param strs:
        :return:
        """
        len_strs = len(strs)
        if len_strs <= 0:
            return ""
        pre = strs[0]
        tail = 1
        while tail < len_strs:
            pre = self.common_prefix(pre, strs[tail])
            if pre == "":
                break
            tail += 1
        return pre

    def common_prefix(self, a, b):
        """
        输入两个字符，返回其公共前缀，不存在则返回""
        :param a:
        :param b:
        :return:
        """
        lena = len(a)
        lenb = len(b)
        size = min(lena, lenb)
        num = 0
        for i in range(size):
            if a[i] != b[i]:
                break
            num += 1
        return a[0:num]
