# -*- coding:utf-8 -*-
# @Time : 2020/8/15 17:04 
# @Author : bendan50
# @File : Q215-find-kth-largest.py 
# @Function : 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# @Software: PyCharm

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        思路：堆排，构建大顶堆
        :param nums:
        :param k:
        :return:
        """
        pass
        num_size = len(nums)
        self.build_max_heap(nums, num_size)  # 初始堆，后面直接走调整就行了。
        for i in range(k):
            # 先互换下，再调整
            self.swap(nums, 0, num_size - i - 1)
            heap_size = num_size - i - 1
            #调整是从0开始。因为堆已经构建好了，与下标0互换后，堆可能改变，所以需要调整。
            self.adjust_heap(nums, 0, heap_size)
        print('nums = {}'.format(nums))
        return nums[num_size - k]

    def build_max_heap(self, nums, heap_size):
        """
        需要不断地去构建堆，而且每次堆的大小都将变化，所以需要作为参数给出。
        构建堆的过程：从第一个非叶子节点开始调整堆（调用adjust_heap函数）
        直到根节点。
        :param nums:
        :param heap_size:
        :return:
        """
        start = heap_size // 2 - 1  # 第一个非叶子节点的下标
        for idx in range(start, -1, -1):
            self.adjust_heap(nums, idx, heap_size)

    def adjust_heap(self, nums: List[int], idx, heap_size):
        """
        调整堆。最大堆满足 x[i] >= x[2*i+1] and x[i] >= x[2*i+2]
        :param nums: 堆，看成是一个完全二叉树
        :param idx: 需要调整的非叶子节点
        :param heap_size: 堆的大小
        :return:
        """
        left = 2 * idx + 1
        right = 2 * idx + 2
        temp = idx
        if left < heap_size and nums[left] > nums[temp]:
            temp = left
        if right < heap_size and nums[right] > nums[temp]:
            temp = right
        if temp != idx:
            # 说明根、左、右三个节点中，根节点不是最大的，需要调整。
            self.swap(nums, temp, idx)
            # 现在需要考虑一个问题（假设互换前左节点最大），互换位置后，原来的根节点变成了原来左子树的根节点
            # 因为左节点最大，现在换成了比之前小的数当根结点，关系 x[i] >= x[2*i+1] and x[i] >= x[2*i+2]可能被破坏了。
            # 所以也需要调整一下，正是因为向下递归，所以前面的if才需要边界判断
            self.adjust_heap(nums, temp, heap_size)
        else:
            # 说明调整结束。
            pass

    def swap(self, nums, idx, idy):
        temp = nums[idx]
        nums[idx] = nums[idy]
        nums[idy] = temp


if __name__ == "__main__":
    nums = [3, 2, 2, 4, 5, 3, 1, 9, 5, 6]
    ret = Solution().findKthLargest(nums, 4)
    print('ret = {}'.format(ret))
