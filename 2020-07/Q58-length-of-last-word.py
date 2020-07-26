# -*- coding:utf-8 -*-
# @Time : 2020/7/26 15:40 
# @Author : bendan50
# @File : Q58-length-of-last-word.py 
# @Function : 最后一个单词的长度
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
# 如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
# 输入: "Hello World"
# 输出: 5
# @Software: PyCharm


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        思路：从尾开始遍历
        :param s:
        :return:
        """
        size = len(s)
        idx = size - 1
        head = tail = idx
        find_word = False
        while idx >= 0:
            if not find_word and s[idx] == ' ':     #没找到单词，空格
                idx -= 1
                continue
            if find_word and s[idx] == ' ':         #找到单词，空格
                pass
                break
            elif find_word:                     #找到单词，非空格
                pass
                tail = idx
            else:                           #没找到单词，非空格
                find_word = True
                head = idx
                tail = idx
            idx -= 1
        return head-tail + 1 if find_word else 0

if __name__ =="__main__":
    s = "a "
    ret = Solution().lengthOfLastWord(s)
    print('ret = {}'.format(ret))