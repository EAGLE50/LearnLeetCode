# -*- coding:utf-8 -*-
# @Time : 2020/7/25 16:00 
# @Author : bendan50
# @File : Q29-divide.py 
# @Function : 两数相除
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
# @Software: PyCharm

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        思路：不能使用除法、乘法、Mod运算，那还能用什么呢？加法和减法？
        一次次减去divisor？这时间会很长的。那么就减去N倍的divisor，但如何去实现表示N倍的divisor呢？
        第一次比较dividend和divisor大小，然后divisor = divisor + divisor,     #2*divisor
        第二次比较dividend和divisor大小,然后divisor = divisor + divisor,      #4*divisor
        第三次比较dividend和divisor大小                                      #8*divisor
        如果在4-8之间怎么办？dividend > 4*divisor and dividend < 8*divisor
        dividend = dividend - 4*divisor继续第一次比较，
        递归出现的！
        :param dividend:
        :param divisor:
        :return:
        """
        MAX = 2**31-1
        MIN = -2**31
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        # 需要处理整数越界问题
        if divisor == -1:
            if dividend > MIN:
                return -dividend
            return MAX
        sign = 1  # 正号
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else -divisor
        ret = self.div(a, b)        #注意需要加正负号
        return ret if sign > 0 else -ret

    def div(self, a, b):
        if a < b:
            return 0
        count = 1  # 商
        tb = b  # b的值不能改变，要保留最初的基准
        while (tb + tb) < a:
            count = count + count
            tb = tb + tb
        return count + self.div(a - tb, b)


if __name__ == "__main__":
    dividend =-2147483648
    divisor =-1
    ret = Solution().divide(dividend,divisor)
    print('ret = {}'.format(ret))
