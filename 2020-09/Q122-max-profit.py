# -*- coding:utf-8 -*-
# @Time : 2020/9/4 21:43 
# @Author : bendan50
# @File : Q122-max-profit.py 
# @Function : 买卖股票的最佳时机 II
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 提示：
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4
# @Software: PyCharm

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        思路：官方的说法叫峰谷法，把上升的区间段的收益相加即可。
        实际上，也可以理解为贪心算法。
        以卖出为例，只要p[i+1]大于p[i]，说明应该继续持有，反过来则需要在p[i]处卖出。
        以买入为例，只要p[i+1]大于p[i]，说明此时应该买入，反过来则需要耐心等待。
        :param prices:
        :return:
        """
        sum = 0
        size = len(prices)
        buy = -1
        sell = -1
        have_stock = False  # 手中是否持有股票
        for i in range(size - 1):  # 保证i+1不越界
            if have_stock:
                if prices[i + 1] < prices[i]:
                    sell = prices[i]
                    sum += sell - buy
                    have_stock = False
                pass
            else:
                if prices[i + 1] > prices[i]:
                    buy = prices[i]
                    have_stock = True
                pass
        if have_stock:  #有股票，说明最后是一直上涨的，最后一天需要卖出
            sell = prices[size - 1]
            sum += sell - buy
        return sum

if __name__ == "__main__":
    # prices = [1,2,3,4,5]
    prices = [1,2]
    ret = Solution().maxProfit(prices)
    print('ret = {}'.format(ret))