# -*- coding:utf-8 -*-
# @Time : 2020/7/12 23:10 
# @Author : bendan50
# @File : Q38-count-and-say.py 
# @Function : 外观数列
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
#
# 描述前一项，这个数是 1 即 “一个 1 ”，记作 11
#
# 描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
#
# 描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
#
# 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221
# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
# @Software: PyCharm

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        思路：需要实现一个描述函数，输入str，输出str，输出是对输入的描述。
        没用递归的标准写法，而是函数调函数。
        :param n:
        :return:
        """
        pre = "1"
        for idx in range(1,n):
            pre = self.desc(pre)
        return pre

    def desc(self, n: str) -> str:
        ret = ""
        pre = n[0]      #待计数的数字
        num = 0     #计数
        for _, ele in enumerate(n):
            if ele == pre:
                num += 1
            else:
                ret = ret + str(num) + pre
                pre = ele
                num = 1
            pass
        ret = ret + str(num) + pre      #处理最后的一个字符
        return ret


if __name__ == "__main__":
    ret = Solution().desc('12345532671')
    print('ret = {}'.format(ret))
    n = 4
    ret = Solution().countAndSay(n)
    print('ret = {}'.format(ret))
