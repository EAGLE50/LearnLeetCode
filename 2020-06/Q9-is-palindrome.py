# -*- coding:utf-8 -*-
# @Time : 2020/6/21 20:53 
# @Author : bendan50
# @File : Q9-is-palindrome.py 
# @Function : 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 输入: 121
# 输出: true
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# @Software: PyCharm


class Solution:
    def is_palindrome_python(self, x: int) -> bool:
        """
        完成使用python语言的解决方案，但不被其他高级语言适用，如C++、Java
        :param x:
        :return:
        """
        str_x = str(x)
        new_x = str_x[::-1]
        print("x = {} and new_x = {}".format(x, new_x))
        return str_x.__eq__(new_x)

    def isPalindrome(self, x: int) -> bool:
        """
        按C++、Java的思路完成。同Q7整数反转，但有越界，所以不能反转全部，可以反转一半
        关键问题在于：如何去判断反转到一半了？当x的位数是偶数时rev_x == x；当位数是奇数时rev_x > x
        边界：负数、个位数是0的正数均不是回文数。
        :param x:
        :return:
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        rev_x = 0
        while x > rev_x:
            rev_x = rev_x * 10 + x % 10
            x = x // 10
        if x == rev_x or (rev_x // 10 == x):
            return True
        else:
            return False


if __name__ == "__main__":
    x = 0
    ret = Solution().isPalindrome(x)
    # ret = Solution().is_palindrome_python(x)
    print('ret = {}'.format(ret))
