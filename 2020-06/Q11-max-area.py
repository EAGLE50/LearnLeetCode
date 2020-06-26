# -*- coding:utf-8 -*-
# @Time : 2020/6/25 16:18 
# @Author : bendan50
# @File : Q11-max-area.py 
# @Function ： 盛最多水的容器
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# @Software: PyCharm

class Solution:
    def max_area(self, height) -> int:
        """
        官方思路实现，使用双指针，时间复杂度O(n)
        从两端向中间压缩，移动高度值小的一侧的下标
        :param height:
        :return:
        """
        max = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = self.crsh_area(start,end,height[start],height[end])
            max = max if max >= area else area
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max
    def maxArea(self, height) -> int:
        """
        思路：暴力法，时间复杂度O(n^2)，超时，不通过
        :param height: list[int]
        :return:
        """
        max = 0
        size = len(height)
        for i in range(size):
            for j in range(i+1,size,1):
                a = self.crsh_area(i,j,height[i],height[j])
                max = max if max > a else a
        return max

    #求面积
    def crsh_area(self,idx_start,idx_end,val_start,val_end):
        val = min(val_start,val_end)
        idx = abs(idx_start - idx_end)
        return val * idx


if __name__ == '__main__':
    heigh = [1,8,6,2,5,4,8,3,7]
    ret_crsh = Solution().maxArea(heigh)
    ret = Solution().max_area(heigh)
    print('ret_crsh = {} and ret = {}'.format(ret_crsh,ret))