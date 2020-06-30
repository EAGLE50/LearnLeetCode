# -*- coding:utf-8 -*-
# @Time : 2020/6/21 22:21 
# @Author : bendan50
# @File : Q13-roman-to-int.py 
# @Function : 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 输入: "III"
# 输出: 3
# 输入: "IX"
# 输出: 9
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# @Software: PyCharm


class Solution:
    def romanToInt(self, s) -> int:
        """
        思路：设置高低级别，与紧邻的下一位比较，若下一位级别高，则表示一个整体（下一位的级别-当前位的级别）
        若下一位级别低，则直接处理当前位即可
        :param s:
        :return:
        """
        roman_map = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        str_len = len(s)
        ret = 0
        if str_len == 1:
            return roman_map.get(s)
        i = 0
        #因为有i+1的存在，所以i最多到str_len-2的位置
        while i < str_len-1:
            a = roman_map.get(s[i])
            b = roman_map.get(s[i+1])
            if a >= b:
                ret += a
                i += 1
            else:
                ret = ret+b-a
                i += 2
        if i == str_len-1:
            # 表示s[str_len-2]s[str_len-1]没有构成一个整体，需要单独计算
            ret += roman_map.get(s[i])
        return ret


if __name__ == "__main__":
    str = 'LVIII'
    ret = Solution().romanToInt(str)
    print(ret)