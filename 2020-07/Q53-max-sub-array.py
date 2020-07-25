# -*- coding:utf-8 -*-
# @Time : 2020/7/24 19:34 
# @Author : bendan50
# @File : Q53-max-sub-array.py 
# @Function : 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# @Software: PyCharm

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        思路：目标是实现复杂度O(n)，所以遍历时，需要用额外空间记点什么。
        从第一个正数开始记录累加值，不管当前所累加的值是正是负。记录的信息是：
        假设10个元素，第5个元素记录的是1-5个元素中最大的子序列和，现在求第6个元素应该记录什么值，来表示1-6个元素中最大的子序列和
        即：F(i) = max{F(i-1)+Ei,Ei}.     F(i)表示以i元素结尾的最大子序列和
        这个公式像什么？动态规划！
        :param nums:
        :return:
        """
        size = len(nums)
        ret = 0
        for idx, ele in enumerate(nums):
            if idx == 0:
                ret = ele
                pre_last = ele
            else:
                n = max(pre_last + ele, ele)  # pre_last相当于F(i-1)，这样就不用用一个数组保存起来了。
                pre_last = n
                ret = max(ret, n)
        pass
        return ret

    def max_SubArray(self, nums: List[int]) -> int:
        """
        进阶：使用分治法求解！
        分治的思路是[start,end]分成两段，即[start,middle]和[middle+1,end]。假设已经知道了[start,middle]和[middle+1,end]
        两个序列的各自的最大子序列和，现在求[start,end]的最大子序列和。怎么求呢？
        不会。。。想不出来。见官方解析，然后从后往前推，希望下次可以想出来。
        思路：问：当合并时，[start,end]的最大子序列有几种情况？这个必须回答全，答：
        第一种情况：以start开头，以temp结束，其中temp <= middle
        第二种情况：以start开头，以temp结束，其中middle < temp < end
        第三种情况：以start开头，以end结束。
        第四种情况：不以start开头，且不以end结束。
        第五种情况：以end结束，以temp开头，其中start < temp <= middle
        第六种情况：以end结束，以temp开头，其中middle < temp < end
        共计六种情况，现在的问题变成了：如何求这六种情况下的最大序列和呢？即，我们需要从[start,middle]和[middle+1,end]中拿到什么信息呢？
        以第一种情况为例，完全是左区间的事，即合并后最大子序列和完全来自左区间。
        那么，我希望有个值来表示以start开头的最大子序列和，记作left_sum
        同理（六种情况），以end为结束的最大子序列和，记作right_sum
        对于第三种情况，我们需要记录区间的所有数的和，记作all_sum，这样，第三种情况的最大子序列和即为左右区间的all_sum相加。
        现在剩下什么了呢？只剩下第二种、第四种、第五种情况，而且第二种和第五种可以与left_sum和right_sum建立关联，
        所以以剩下第四种情况！将这个最大序列和记作mid_sum，表示中间区间内的最大子序列和。
        综上：我整理下，看看我有哪些数据。
        以左区间[start,middle]为例，我知道的数据如下：
        left_sum:   以start开头，即必须包含start点，且为第一个点的最大序列和
        right_sum:  以middle结束，即必须包含end点，且为最后一个点的最大序列和
        all_sum:    序列[start,middle]的和，即累加求和的结果
        mid_sum:    (start,middle)区间的最大子序列和，即不包含start点和end点的最大子序列和
        用这四个数据，如何合并呢，来处理六种情况？
        合并后left_sum = MAX(左区间left_sum，左区间all_sum+右区间left_sum)   #对应第一、二种情况
        合并后right_sum = MAX(右区间right_sum，右区间all_sum+左区间right_sum)    #对应第五、六种情况
        合并后all_sum = 左区间all_sum + 右区间all_sum        #对应第三种情况
        合并后mid_sum = MAX(左区间mid_sum，右区间mid_sum，左区间right_sum+右区间left_sum)      #对应第四种情况
        注：官方解析中提到了“线段树”的结构！
        :param nums:
        :return:
        """
        size = len(nums)
        ret = self.recursion(nums, 0, size - 1)
        print('==={}==='.format(ret))
        return max(ret)
        pass

    def recursion(self, nums, start, end):
        if start == end:
            left_sum = right_sum = all_sum = mid_sum = nums[start]
            return left_sum, right_sum, all_sum, mid_sum
        mid = (start + end) // 2
        left_area = self.recursion(nums, start, mid)
        right_area = self.recursion(nums, mid + 1, end)
        left_sum = max(left_area[0], left_area[2] + right_area[0])
        right_sum = max(right_area[1], right_area[2] + left_area[1])
        all_sum = left_area[2] + right_area[2]
        temp = max(left_area[3], right_area[3])
        mid_sum = max(temp, left_area[1] + right_area[0])
        return left_sum, right_sum, all_sum, mid_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ret = Solution().maxSubArray(nums)
    ret2 = Solution().max_SubArray(nums)
    print('ret = {} and ret2 = {}'.format(ret, ret2))
