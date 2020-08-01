# -*- coding:utf-8 -*-
# @Time : 2020/8/1 10:57 
# @Author : bendan50
# @File : Q415-add-strings.py 
# @Function : 字符串相加
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 注意：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# @Software: PyCharm

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1_size = len(num1)
        n2_size = len(num2)
        pre = '0'
        ret = ''
        while n1_size > 0 and n2_size > 0:
            a = num1[n1_size - 1]
            b = num2[n2_size - 1]
            sum = int(a) + int(b) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n1_size -= 1
            n2_size -= 1
        while n1_size > 0:
            a = num1[n1_size - 1]
            sum = int(a) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n1_size -= 1
        while n2_size > 0:
            b = num2[n2_size - 1]
            sum = int(b) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n2_size -= 1
        if pre != '0':
            ret = pre + ret
        return ret