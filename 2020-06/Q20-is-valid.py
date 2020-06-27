# -*- coding:utf-8 -*-
# @Time : 2020/6/27 20:33 
# @Author : bendan50
# @File : Q20-is-valid.py 
# @Function : 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# @Software: PyCharm


class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = []
        pre = ['(','{','[']
        back = [')','}',']']
        size = len(s)
        if size % 2 != 0:
            return False
        for i,c in enumerate(s):
            print('i = {} and c = {}'.format(i,c))
            if c in pre:
                str_stack.append(c)
            else:
                #注：不能直接pop取栈顶元素，容易抛空针，所以需要先检查是否为空
                if len(str_stack) == 0:
                    return False
                tail = str_stack.pop()
                if pre.index(tail) != back.index(c):
                    return False
        return len(str_stack) == 0


if __name__ == '__main__':
    ret = Solution().isValid('[')
    print(ret)