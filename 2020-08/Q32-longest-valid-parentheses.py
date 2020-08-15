# -*- coding:utf-8 -*-
# @Time : 2020/7/16 20:41 
# @Author : bendan50
# @File : Q32-longest-valid-parentheses.py 
# @Function : 最长有效括号
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# @Software: PyCharm

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        思路：字符'('则进栈，继续遍历；字符')'则出栈，出栈时，若匹配，则记录个数后继续遍历；若不匹配，清空栈后继续遍历
        s = "()(()"
        s = "())()"
        这就是为什么'('进栈时需要的特殊处理，而不是直接进栈就完事了。
        :param s:
        :return:
        """
        stack = [-1]  # 数组模拟栈,里面存储下标！
        ret = 0
        for idx, ele in enumerate(s):
            if ele == '(':
                stack.append(idx)
            else:
                st = stack.pop()
                if stack.__len__() == 0:        #空栈
                    stack.append(idx)
                else:
                    temp = idx - stack[stack.__len__() - 1]
                    ret = max(ret,temp)
        pass
        return ret


if __name__ == "__main__":
    # s = ")()())))()(()(()(()))()()()((())))"        #26
    # s = "(()"
    s = "()(()"
    ret = Solution().longestValidParentheses(s)
    print('ret = {}'.format(ret))
