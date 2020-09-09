# -*- coding:utf-8 -*-
# @Time : 2020/9/9 18:53 
# @Author : bendan50
# @File : Q134-can-complete-circuit.py 
# @Function : 加油站
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
# 你从其中的一个加油站出发，开始时油箱为空。
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
# 说明: 
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
# 示例 1:
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# 示例 2:
# 输入:
# gas  = [2,3,4]
# cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
# @Software: PyCharm

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        思路：暴力。暴力指两层遍历加油站。第一层遍历起点，第二层遍历能达到的最远距离
        :param gas:
        :param cost:
        :return:
        """
        all_gas = sum(gas)
        all_cost = sum(cost)
        if all_cost > all_gas:
            return -1
        # 尝试寻找可能的起点
        nums = len(gas)
        for i in range(nums):
            flag = True
            have_gas = gas[i]
            j = i + 1
            while j % nums != i:
                loss_cost = cost[(j - 1) % nums]
                if have_gas >= loss_cost:  # 能到达下一个加油站
                    have_gas = have_gas - loss_cost + gas[j % nums]
                else:
                    flag = False
                    break
                pass
                j += 1
            if flag:
                return i
        return -1

    def can_CompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        思路：好吧，我承认。使用贪心算法，可以达到O(n)的时间复杂度，而在看解析之前，我未想清楚。
        现在看到有O(n)的解法，让我重新来思考。
        如果从加油站A到加油站F无法到达，那么从加油站A的下一个加油站B开始，能达到加油站F吗？
        回答能简单：不能！
        因为能从A到B，比从B直接出发，这两种情况下在B点的油量，肯定是前者多。
        既然油多的都到达不了F，那么油少的B肯定也无法到达F。
        那么下一个该考虑可能做为起点的就是F了。
        :param gas:
        :param cost:
        :return:
        """
        all_gas = sum(gas)
        all_cost = sum(cost)
        if all_cost > all_gas:
            return -1
        # 尝试寻找可能的起点
        nums = len(gas)
        start = 0
        while start < nums:
            flag = True
            have_gas = gas[start]
            j = start + 1
            while j % nums != start:
                loss_cost = cost[(j - 1) % nums]
                if have_gas >= loss_cost:  # 能到达下一个加油站
                    have_gas = have_gas - loss_cost + gas[j % nums]
                else:
                    flag = False
                    start = j - 1  # 因为最外层循环有个start+=1
                    break
                pass
                j += 1
            if flag:
                return start
            start += 1
        return -1


if __name__ == "__main__":
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    ret = Solution().canCompleteCircuit(gas, cost)
    print('ret = {}'.format(ret))
