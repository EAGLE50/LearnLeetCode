# -*- coding:utf-8 -*-
# @Time : 2020/7/12 11:40 
# @Author : bendan50
# @File : Q202-is-happy.py
# @Function： 快乐数
# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
#
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# @Software: PyCharm

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        思路：分解一个正整数，很简单，然后重复分解即可，可问题是：如何判断循环停止呢，当不是快乐数时？
        解决：把每个数都记录下来？只要这个数之前出现过，那么经过数次之后，这个数还会出现。
        除了记录下来之外呢？策略同Q141，一快一慢，只要两数相同
        :param n:
        :return:
        """
        slow = fast = n
        while fast != 1:
            slow = self.happy_util(slow)
            fast = self.happy_util(self.happy_util(fast))
            if fast != 1 and slow == fast:
                return False
        return True

    def happy_util(self,n)->int:
        """
        分解n，计算每个位置上的数字的平方和
        :param n:
        :return:
        """
        sum = 0
        while n != 0:
            a = n % 10
            n = n // 10
            sum += a**2
        return sum

if __name__ == "__main__":
    util = Solution().happy_util(19)
    print('util = {}'.format(util))
    ret = Solution().isHappy(10)
    print('ret = {}'.format(ret))
