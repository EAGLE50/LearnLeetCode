# -*- coding:utf-8 -*-
# @Time : 2020/6/23 21:55 
# @Author : bendan50
# @File : Q3-length-of-longest-substring.py 
# @Function : 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# @Software: PyCharm


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        思路：时间复杂度O(n).双指针，从头开始找，记录最大长度，滑动窗口大小只会增加
        :param s:
        :return:
        """
        pre_idx = 0
        tail = -1      #tail记录重复元素最大的下标
        idx = 1
        max = 0
        size = len(s)
        if size <= 1:
            return size
        while idx < size:
            str = s[pre_idx:idx]
            c = s[idx]
            c_t = str.rfind(c)   # c在str中的位置，注：不能是str.find(c)因为它是寻找第一个，应该记录最后一个！
            if str.find(c) == -1 and pre_idx > tail:
                # 没有找到
                max += 1
                idx += 1
            else:
                # 找到了，有重复元素
                c_t += pre_idx
                tail = tail if tail > c_t else c_t      #pre_idx<tail<idx必有重复元素
                idx += 1
                pre_idx += 1    #保持滑动窗口大小不变
                pass
        pass
        return max+1


if __name__ == "__main__":
    # s = 'aabcd'
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    # s = "aabaab!bb"
    s = "ruowzgiooobpple"
    ret = Solution().lengthOfLongestSubstring(s)
    print('ret = %s'%ret)