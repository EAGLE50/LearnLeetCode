# -*- coding:utf-8 -*-
# @Time : 2020/7/26 16:28 
# @Author : bendan50
# @File : Q66-plus-one.py 
# @Function : 加一
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# @Software: PyCharm

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        思路：很简单，从低位开始加一，当进位为零时停止。但有个疑惑，当最高位需要进位时，超出了数组长度，要平移，
        该怎样去考量这个时间呢？
        :param digits:
        :return:
        """
        pre = 1     #进位，也相当于加 1
        size = len(digits)
        while size > 0 and pre != 0:
            a = digits[size - 1]
            sum = a + pre
            pre = sum // 10
            digits[size - 1] = sum % 10
            size -= 1
        if pre != 0:
            digits.insert(0,pre)
        return digits

if __name__ == "__main__":
    digits = [9]
    ret = Solution().plusOne(digits)
    print('ret = {}'.format(ret))