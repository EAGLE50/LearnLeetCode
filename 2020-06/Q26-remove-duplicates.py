# -*- coding:utf-8 -*-
# @Time : 2020/6/25 13:57 
# @Author : bendan50
# @File : Q26-remove-duplicates.py 
# @Function : 删除排序数组中的重复项
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# @Software: PyCharm

class Solution:
    """
    解题历程：
    思路一：一个个移动数组元素，结果：超时，失败。
    思路二：一个性移动多个数组元素，结果：自我放弃，失败
    思路三：官方推荐。一句话：在双指针的策略下，不要净想着移动数组！！！不要移动数组！！
        只做元素互换！！只做元素互换！！！
    """
    def remove_duplicates_best(self, nums):
        """
        官方思路解法。在提交4次失败后，果断进行学习，变换思路。
        依然是双指针，但代码比我优雅多了。
        注：与我的思路差异点在于：仅需要互换不同的元素即可，即些相同的结点，不要移动它。
        :param nums:
        :return:
        """
        pre_idx = 0
        idx = 1
        nums_len = len(nums)
        while idx < nums_len:
            if nums[pre_idx]== nums[idx]:
                idx +=1
            else:
                pre_idx += 1
                nums[pre_idx]=nums[idx]
        return pre_idx+1

    def remove_duplicates(self, nums) -> int:
        """
        错误代码，未能跑通。思路错误，一次移动多个也不行。
        :param nums:
        :return:
        """
        pre_idx = 0
        idx = 1
        num_len = len(nums)
        # 当数组至多有一个元素时，直接返回数组长度
        if num_len <= 1:
            return num_len
        # 此时数组至少有两个元素
        while idx < num_len:
            if nums[pre_idx] == nums[idx]:
                while idx < num_len - 1 and nums[pre_idx] == nums[idx]:
                    idx += 1
                # 先判断idx是否是最后一个元素
                if idx == num_len - 1:
                    return pre_idx + 1
                i = pre_idx + 1
                j = idx
                while j < num_len:
                    nums[i] = nums[j]
                    i += 1
                    j += 1
                size = idx - pre_idx - 1  # 本次需要一次性移动的元素个数，至少是一个
                num_len -= size
                pre_idx += 1
                idx = pre_idx + 1
            else:
                pre_idx += 1
                idx += 1
        return idx

    def removeDuplicates(self, nums) -> int:
        """
        思路：一个个移动则必定超时，失败！得找到一次性移动多个的方法。
        :param nums:
        :return:
        """
        pre_idx = 0
        idx = 1
        nums_len = len(nums)
        # 当数组至多有一个元素时，直接返回数组长度
        if nums_len <= 1:
            return nums_len
        # 此时数组至少有两个元素
        while idx < nums_len:
            if nums[pre_idx] == nums[idx]:
                # 先判断idx是否是最后一个元素
                if idx == nums_len - 1:
                    return idx
                # 直接移动元素
                for i in range(idx, nums_len - 1, 1):
                    nums[i] = nums[i + 1]
                    pass
                nums_len -= 1
            else:
                pre_idx += 1
                idx += 1
        return idx


if __name__ == "__main__":
    # nums = [1, 1, 1]
    # nums = [1, 1, 2]
    # nums = [1, 1]
    nums = [0,0,1,1,1,2,2,3,3,4]
    ret = Solution().remove_duplicates_best(nums)
    print(ret)
    print(nums[0:ret])
