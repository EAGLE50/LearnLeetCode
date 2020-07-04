# -*- coding:utf-8 -*-
# @Time : 2020/6/29 23:03 
# @Author : bendan50
# @File : Q42-trap.py 
# @Function : 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# @Software: PyCharm

class Solution:
    def trap(self, height) -> int:
        """
        思路：自己能想到的是O(n)的时间复杂度，类似Q121买卖股票的，一前一向组成区间。
        当前值小于等于后值时，该前值有效，即以此前值为边的情况下，可能接下雨水；
        当前值大于后值时，需要找到后值中最大的值。以此构建区域，判断是否能接下雨水；
        当前值遍历到底时才结束。
        :param height:
        :return:
        """
        size = len(height)
        head = 0  # 前值
        tail = 1  # 后值
        max = 1  # 记录自前值往后中小于前值的最大值。
        area = 0  # 前后两值之间柱子的面积
        sum = 0  # 接雨水总量
        while head < size - 1:      #前值只需要遍历到倒数第二个即可
            tail = head + 1
            max = head + 1
            flag = False  # 记录当前head是否作为最小边
            while tail < size:
                if height[head] <= height[tail]:
                    flag = True
                    temp = min(height[head], height[tail]) * (tail - head - 1)
                    area = self.get_area(height, head, tail)
                    sum = sum + (temp - area)
                    head = tail
                    flag = False
                    max = head + 1  # 更新
                    tail = head + 1
                    pass
                else:
                    max = tail if height[tail] > height[max] else max
                    tail += 1
                pass
            if not flag and max < size:
                # 此时，head需要作为最大边
                temp = min(height[head], height[max]) * (max - head - 1)
                area = self.get_area(height, head, max)
                sum = sum + (temp - area)
                head = max
            else:
                head += 1
        pass
        return sum

    def get_area(self, height, head, tail):
        """
        求height[tail]和height[head]之间值的和
        :param height:
        :param head:
        :param tail:
        :return:
        """
        area = 0
        i = head + 1
        while i < tail:
            area += height[i]
            i += 1
        return area


if __name__ == "__main__":
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    height = [2,0,2]
    # height = [4,2,3,9,4,0,2,5,8,1]
    ret = Solution().trap(height)
    print(ret)
