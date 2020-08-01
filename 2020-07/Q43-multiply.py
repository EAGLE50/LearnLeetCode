# -*- coding:utf-8 -*-
# @Time : 2020/7/21 22:51 
# @Author : bendan50
# @File : Q43-multiply.py 
# @Function : 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# @Software: PyCharm

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        思路：暴力法，完全模拟乘法操作即可，涉及字符串相加，注意补零即可。
        :param num1:
        :param num2:
        :return:
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ret = ''
        num2 = num2[::-1]
        for idx, ele in enumerate(num2):
            if ele == '0':
                continue
            t = self.ele_multiply(num1, int(ele))
            ret = self.str_add(ret, t + "0" * idx)
        pass
        return ret

    def ele_multiply(self, num: str, ele: int) -> str:
        ret = ''
        pre = 0
        num = num[::-1]
        for i, n in enumerate(num):
            a = int(n) * ele + pre
            pre = a // 10
            ret = str(a % 10) + ret
        if pre != 0:
            ret = str(pre) + ret
        return ret

    def str_add(self, n1: str, n2: str):
        n1_size = len(n1)
        n2_size = len(n2)
        pre = '0'
        ret = ''
        while n1_size > 0 and n2_size > 0:
            a = n1[n1_size - 1]
            b = n2[n2_size - 1]
            sum = int(a) + int(b) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n1_size -= 1
            n2_size -= 1
        while n1_size > 0:
            a = n1[n1_size - 1]
            sum = int(a) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n1_size -= 1
        while n2_size > 0:
            b = n2[n2_size - 1]
            sum = int(b) + int(pre)
            pre = str(sum // 10)
            ret = str(sum % 10) + ret
            n2_size -= 1
        if pre != '0':
            ret = pre + ret
        return ret

    def multiply_offical(self, num1: str, num2: str) -> str:
        """
        思路：优化竖式。结果的位数小于等于M+N.比如999*99=98901，即3+2=5
        num1[i]*num2[j] = temp
        ret[i+j] = temp // 10
        ret[i+j+1] = temp % 10
        :param num1:
        :param num2:
        :return:
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ret = ''
        n1_size = len(num1)
        n2_size = len(num2)
        ret = '0' * (n1_size + n2_size)
        ret = list(ret)
        idx1 = n1_size - 1
        idx2 = n2_size - 1
        while idx1 >= 0:
            a = int(num1[idx1])
            idx2 = n2_size - 1
            while idx2 >= 0:
                b = int(num2[idx2])
                sum = a * b + int(ret[idx1 + idx2 + 1])
                ret[idx1 + idx2 + 1] = str(sum%10)
                ret[idx1 + idx2] = str(int(ret[idx1 + idx2]) + sum // 10)
                idx2 -= 1
            idx1 -= 1
        pass
        if ret[0] == '0':
            ret.pop(0)
        return "".join(ret)     #list->str


if __name__ == "__main__":
    num1 = "9"
    num2 = "9"
    ret = Solution().multiply(num1, num2)
    ret2 = Solution().multiply_offical(num1, num2)
    print('ret = {}'.format(ret))
    print('ret2 = {}'.format(ret2))
