# -*- coding:utf-8 -*-
# @Time : 2020/7/12 21:49 
# @Author : bendan50
# @File : Q763-partition-labels.py 
# @Function : 划分字母区间
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
# 返回一个表示每个字符串片段的长度的列表。
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
# @Software: PyCharm

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        思路：笨办法，从第一个字符开始，然后往后遍历，查找是否有与第一个字符相同，如果找到了，则分段的尾指针后移至这个位置；
        如果到结尾都没有找到，则第一个字符就可以单独成为一段了。但问题是，如果找到了，接下来的判断就不能只与第一个字符相比较，
        而是需要与第一个段内的所有字符相比较。
        结果：超出时间限制
        改进：笨办法的思路是正确的，也是官方的思路。但问题是，如果找到了，接下来判断的是第一个段内的所有字符。
        我之前的方法，是取这些字符，转为字典，然后重复过程。有改进吗？或者说，查找是否与第一个字符相同的目的是什么呢？
        是找到这个字符最后出现的位置，然后划分出一个字符段来！那么，我们可以将该字符最后一次出现的下标先记录下来，
        比如，我们现在第一个字符是'c'，我们可以直接定位到'c'最后出现的位置，这个区间就是一个字符段。
        然后，在这个字符段内更新最后出现的位置，当遍历下标与最后出现的下标相同时，说明划分成功。
        详见：partition_labels()
        :param S:
        :return:
        """
        head = mid = tail = 0
        size = len(S)
        ret = []
        while head < size:
            vals = set()  # 记录段所包含的字母集合
            vals.add(S[head])
            temp = set()  # 记录可能段所包含的字母集合
            temp.add(S[head])
            flag = False
            tail = head + 1
            while tail < size:
                ele = S[tail]
                if not flag and ele in vals:
                    mid = tail
                    flag = True
                    # 更新temp集合
                    temp = set(list(S[head:mid+1]))
                if flag and ele in temp:
                    mid = tail
                    temp = set(list(S[head:mid + 1]))
                tail += 1
            ret.append(mid - head + 1)
            head = mid + 1
        pass
        return ret

    def partition_labels(self, S: str) -> List[int]:
        """
        时间复杂度O(n) 空间复杂度O(n)
        :param S:
        :return:
        """
        last_ele_idx = {}
        for idx,ele in enumerate(S):
            last_ele_idx.__setitem__(ele,idx)
        size = len(S)
        ret = []
        head = 0
        while head < size:
            tail = head
            last = last_ele_idx.get(S[tail])
            while tail < last:
                temp = last_ele_idx.get(S[tail])
                last = max(temp,last)
                tail += 1
            ret.append(tail-head+1)
            head = tail+1
        return ret

if __name__=="__main__":
    S = "ababcbacadefegdehijhklij"
    S = "caedbdedda"
    ret = Solution().partitionLabels(S)
    ret2 = Solution().partition_labels(S)
    print('ret = {}'.format(ret))
    print('ret2 = {}'.format(ret2))
    seq = S[0:9]
    print('list_s = {}'.format(seq))
    list_seq = list(seq)
    print('list_seq = {}'.format(list_seq))
    set_seq = set(list_seq)
    print('set_seq = {}'.format(set_seq))
