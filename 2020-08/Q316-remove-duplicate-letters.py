# -*- coding:utf-8 -*-
# @Time : 2020/7/16 20:51 
# @Author : bendan50
# @File : Q316-remove-duplicate-letters.py 
# @Function : 去除重复字母
# 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
# 需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）
# 输入: "bcabc"
# 输出: "abc"
# 输入: "cbacdcbc"
# 输出: "acdb"
# @Software: PyCharm

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        思路：在遍历字符串的过程中，如果字符 i 大于字符i+1，在字符 i 不是最后一次出现的情况下，删除字符 i
        然后借助栈，完成一次遍历。
        关于是不是最后一次出现，官方采用了最后一个下标法。
        :param s:
        :return:
        """
        count = {}
        stack = []
        ret_set = set()
        # 第一次遍历，记录各字符出现的次数
        for _, ele in enumerate(s):
            val = count.get(ele)
            if val:
                count.__setitem__(ele, val + 1)
            else:
                count.setdefault(ele, 1)
        pass
        print('count = {}'.format(count))
        # 第二次遍历
        for _, ele in enumerate(s):
            size = len(stack)
            if size == 0:
                stack.append(ele)
                ret_set.add(ele)
                continue
            if ret_set.__contains__(ele):  # 已经在栈里了，将出现次数减一，更新后面出现的次数。
                old_val = count.get(ele)
                count.__setitem__(ele, old_val - 1)
                continue
            flag = True
            while flag and size > 0:
                top = stack[size - 1]
                num = count.get(top)
                if top > ele and num > 1:
                    rm_num = stack.pop()
                    ret_set.discard(rm_num)  # 因为出栈，所以集合也应该去掉
                    count.__setitem__(top, num - 1)
                    size = len(stack)
                else:
                    stack.append(ele)
                    ret_set.add(ele)
                    flag = False
            if flag:  # 因size=0退出while循环，还未入栈
                stack.append(ele)
                ret_set.add(ele)
        return "".join(stack)

    def remove_DuplicateLetters(self, s) -> int:
        """
        官方实现，简捷多了。一样的思路，别人的代码一点也不臃肿。
        :param s:
        :return:
        """
        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


if __name__ == "__main__":
    # s = 'cbacdcbc'
    s = "bbcaac"
    ret = Solution().removeDuplicateLetters(s)
    print('ret = {}'.format(ret))
