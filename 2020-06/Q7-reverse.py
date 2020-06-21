# -*- coding:utf-8 -*-
# @Time : 2020/6/21 19:57 
# @Author : bendan50
# @File : Q7-reverse.py 
# @Function : 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。
# 输入: 123
# 输出: 321
# 输入: -123
# 输出: -321
# 输入: 120
# 输出: 21
# @Software: PyCharm


class Solution:
    """
    思路：很清晰，取出最后一个数，将新数乘以10再加上刚才取的数，即为新数。
    关键点：边界的判断。此处查看了解析。有python语言的基础实现和其他语言的巧妙实现。
    """
    def reverse(self, x: int) -> int:
        flag = True
        if x > 0:
            t = x
            flag = True
            boundary = (1<<31) - 1
        elif x < 0:
            t = -x
            flag = False
            boundary= (1<<31)
        else:
            return x
        sum = 0
        #print('boundary = {}'.format(boundary))
        while t:
            a = t % 10  #取t的最后一位
            sum = 10 * sum + a
            t = t // 10
            # 这个判断的增加是查看了解析，网友“twobugs”提供的方法，判断是否越界.但对python语言不好使
            # if ((sum * 10) / 10) != sum:
            #     return 0
            if sum > boundary:
                return 0
        if flag:
            return sum
        else:
            return sum * -1


if __name__ == "__main__":
    x = 1534236469
    ret = Solution().reverse(x)
    print("x = {} and ret = {}".format(x,ret))
