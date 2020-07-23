# -*- coding:utf-8 -*-
# @Time : 2020/7/21 23:02 
# @Author : bendan50
# @File : Q258-add-digits.py 
# @Function : 各位相加
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
# @Software: PyCharm

class Solution:
    def addDigits(self, num: int) -> int:
        """
        思路：采用递归，试下。
        :param num:
        :return:
        """
        if num // 10 == 0:
            return num
        add_sum = self.add(num)
        return self.addDigits(add_sum)
        pass
    def add(self,num:int)->int:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum

    def add_digits(self,num):
        """
        思路：进阶，O(1)的时间复杂度。
        想一下，它可能的值有几种？答：十种，而且除了0，其他数值的结果只能是1-9之间。那么有规律不？1-9之间的规律？
        看下，1到30的结果：
        1、2、3、4、5、6、7、8、9、  【1-9】
        1、2、3、4、5、6、7、8、9、  【10-18】
        1、2、3、4、5、6、7、8、9、  【19-27】
        发现规律了不？     9个数一循环，所以模9的操作避免不了。
        综上：
        if num ==0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        简化代码： return (num - 1) % 9 + 1      #注：python语言不行，Java是可以的。
        原因：在python中 -1%9=8      在Java中-1%9=-1
        :param num:
        :return:
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

if __name__ == "__main__":
    num = 0
    ret = Solution().addDigits(num)
    ret2 = Solution().add_digits(num)
    print('ret = {} and ret2 = {}'.format(ret,ret2))