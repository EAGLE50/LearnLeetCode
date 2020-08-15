# -*- coding:utf-8 -*-
# @Time : 2020/7/16 20:49 
# @Author : bendan50
# @File : Q224-calculate.py 
# @Function : 基本计算器
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
# 输入: "1 + 1"
# 输出: 2
# 输入: " 2-1 + 2 "
# 输出: 3
# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
# @Software: PyCharm

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """
        思路：使用栈来对二元运算中的二元进行配对。入栈时，如果栈顶是+/-则进行运算，然后再将计算结果入栈
        又因为是字符串，决定遍历两次，第一次用于拆分出字符数字来，第二次再计算
        :param s:
        :return:
        """
        stack = []
        cal = []
        num = ''
        for i, ele in enumerate(s):
            if ele in [' ', '+', '-', '(', ')']:
                # 前面一个数已经分离出来了
                if num != '':
                    stack.append(num)
                    num = ''
                if ele != ' ':
                    stack.append(ele)
            else:
                num += ele
        pass
        if num != '':
            stack.append(num)
        # 完成拆分，接下来开始计算
        print('stack = {}'.format(stack))
        for _, ele in enumerate(stack):
            if ele in ['(', '+', '-']:
                cal.append(ele)
            elif ele == ')':
                top_num = cal.pop()
                flag = cal.pop()  # flag = '('
                self.append_num(cal, top_num)
            else:  # ele是数字，如果栈顶是+/-，则需要计算，其他直接放
                self.append_num(cal, ele)
        return cal.pop()

    def append_num(self, cal: List, ele: str):
        if len(cal) == 0:
            cal.append(ele)
        else:
            top = cal[len(cal) - 1]
            if top == '(':
                cal.append(ele)
            elif top == '+':
                flag = cal.pop()  # flag = '+'
                str_a = cal.pop()
                ret = self.add_str(str_a, ele)
                cal.append(ret)
            else:
                flag = cal.pop()  # flag = '-'
                str_a = cal.pop()
                ret = self.sub_str(str_a, ele)
                cal.append(ret)

    # 字符串加法
    def add_str(self, str_a, str_b):
        ret = int(str_a) + int(str_b)
        return str(ret)

    # 字符串减法
    def sub_str(self, str_a, str_b):
        ret = int(str_a) - int(str_b)
        return str(ret)


if __name__ == '__main__':
    s = "1 + 1"
    ret = Solution().calculate(s)
    print('ret = {}'.format(ret))
