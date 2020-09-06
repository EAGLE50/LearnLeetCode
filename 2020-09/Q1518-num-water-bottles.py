# -*- coding:utf-8 -*-
# @Time : 2020/9/6 17:55 
# @Author : bendan50
# @File : Q1518-num-water-bottles.py 
# @Function : 换酒问题
# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
# 请你计算 最多 能喝到多少瓶酒。
# @Software: PyCharm

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        思路：很简单，用机器一次次模拟就可以了。
        :param numBottles:
        :param numExchange:
        :return:
        """
        sum = numBottles
        null_bottles = numBottles
        while null_bottles >= numExchange:
            tmp = null_bottles // numExchange
            sum += tmp
            null_bottles = null_bottles - tmp * numExchange + tmp
        return sum

    def num_WaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        思路：很显然，上面的模拟是有规则的，可以转化为数学公式，用一行代码解决。
        e个瓶子可以换回1个瓶子，相当于每次损失e-1个瓶子。
        现在初始有b个瓶子，每次损失e-1个瓶子，可以损失几次？
        n = b / (e-1)  取下整
        即为：n = (b-e)//(e-1)+1
        :param numBottles:
        :param numExchange:
        :return:
        """
        return (numBottles - numExchange) // (
                    numExchange - 1) + 1 + numBottles if numBottles >= numExchange else numBottles
