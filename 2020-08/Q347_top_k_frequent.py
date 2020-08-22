# -*- coding:utf-8 -*-
# @Time : 2020/8/22 15:58 
# @Author : bendan50
# @File : Q347_top_k_frequent.py 
# @Function : 前 K 个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]
# 提示：
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
# @Software: PyCharm

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        思路：创建一个集合和一个字典，统计每个数出现的次数，然后再排序
        :param nums:
        :param k:
        :return:
        """
        num_dict = self.get_ele_num(nums)
        print('num_dict = {}'.format(num_dict))
        # 排序，也可以使用桶排序
        ret = []
        n = len(num_dict)  # 有几个不同的数
        self.build_max_head(num_dict)
        print('num_dict = {}'.format(num_dict))
        for i in range(k):
            temp = num_dict[0]
            self.swap(num_dict,0,n-1-i)
            (k,v),=temp.items()
            ret.append(k)
            self.adjust_head(num_dict, 0, n - i - 1)
        return ret

    def get_ele_num(self, nums: List[int]) -> List[dict]:
        ele_set = set()
        ret = []
        idx_dict = dict()  # 用来记录ele在ret列表中的下标，可用来直接更新出现次数
        for _, ele in enumerate(nums):
            if ele in ele_set:
                t_dct = ret[idx_dict.get(ele)]
                t_dct.__setitem__(ele, t_dct.get(ele) + 1)
                ret[idx_dict.get(ele)] = t_dct
            else:
                idx_dict.setdefault(ele, len(ret))
                t = dict()
                t.__setitem__(ele, 1)
                ret.append(t)
                ele_set.add(ele)
        return ret

    def build_max_head(self, num_dict: List[dict]):
        """
        构建大顶堆，从最后一个非叶子节点开始。idx = size//2-1
        注意求idx时，size是大小，而不是最后一个下标
        :param num_dict:
        :return:
        """
        size = len(num_dict)
        for i in range(size // 2 - 1, -1, -1):
            self.adjust_head(num_dict, i, size)
        pass

    def adjust_head(self, num_dict: List[dict], start: int, size: int):
        """
        调整堆
        :param num_dict:
        :param start: 是下标
        :param size: 是堆大小，不是最后的一个下标
        :return:
        """
        temp = start
        left = 2*start+1
        right = 2*start+2
        if left < size and self.compare_dict(num_dict[temp],num_dict[left]):
            temp = left
        if right < size and self.compare_dict(num_dict[temp],num_dict[right]):
            temp = right
        if temp != start:
            self.swap(num_dict,start,temp)
            self.adjust_head(num_dict,temp,size)
        pass

    def compare_dict(self,dict1:dict,dict2):
        (k1,v1), = dict1.items()
        (k2,v2), = dict2.items()
        return True if v1 < v2 else False
    def swap(self,num_dict,idx,idy):
        temp = num_dict[idx]
        num_dict[idx] = num_dict[idy]
        num_dict[idy] = temp


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    ret = Solution().topKFrequent(nums, 2)
    print('ret = {}'.format(ret))
    # test = dict()
    # test.__setitem__(3,1)
    # (key,val), = test.items()
    # print(test.keys())
    # print(test.values())
    # print('key = {}'.format(key))
