# -*- coding:utf-8 -*-
# @Time : 2020/7/2 20:32 
# @Author : bendan50
# @File : Q121-max-profit.py
# @Function ： 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0
# @Software: PyCharm

class Solution:
    def maxProfit(self, prices) -> int:
        """
        思路：双指针，记录买入和卖出。当卖出为-1时，表示没有完成交易
        :param prices:
        :return:
        """
        nums_len = len(prices)
        buy_idx = 0
        sell_idx = -1
        tail_idx = buy_idx + 1
        max = 0
        while tail_idx < nums_len:
            if prices[buy_idx] < prices[tail_idx]:
                temp = prices[tail_idx] - prices[buy_idx]
                if temp > max:
                    max = temp
                    sell_idx = tail_idx     #更新卖出点
                tail_idx += 1
                pass
            else:
                buy_idx = tail_idx  #buy_idx表示买入最便宜
                tail_idx += 1
        pass
        if sell_idx == -1:
            return 0
        else:
            return max