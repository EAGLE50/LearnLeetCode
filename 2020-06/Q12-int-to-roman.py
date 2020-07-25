# -*- coding:utf-8 -*-
# @Time : 2020/6/21 22:21
# @Author : bendan50
# @File : Q12-int-to-roman.py 
# @Function : 整数转罗马数字
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# @Software: PyCharm

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        思路：从尾开始取位，然后与5判断。遍历时记住位，即是十位还是百位或是千位，其与截取的次数关系是10^n
        :param num:
        :return:
        """
        roman_map = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        n = 0  # 10^n 幂次
        ret = ""
        while num > 0:
            ele = num % 10
            if ele == 5:
                str = roman_map.get(ele * 10 ** n)
                ret = str + ret
            elif ele == 1 or ele == 2 or ele == 3:
                c = roman_map.get(1 * 10 ** n)
                ret = c * ele + ret
            elif ele == 4:
                c_5 = roman_map.get(5 * 10 ** n)
                c_1 = roman_map.get(1 * 10 ** n)
                ret = c_1 + c_5 + ret
            elif ele == 9:
                c_10 = roman_map.get(10 * 10 ** n)
                c_1 = roman_map.get(1 * 10 ** n)
                ret = c_1 + c_10 + ret
            elif ele == 6 or ele == 7 or ele == 8:
                c_5 = roman_map.get(5 * 10 ** n)
                c_1 = roman_map.get(1 * 10 ** n)
                ret =  c_5 + c_1 * (ele - 5) + ret
            num = num // 10
            n += 1
        pass
        return ret


if __name__ == "__main__":
    num = 1994
    ret = Solution().intToRoman(num)
    print('ret = {}'.format(ret))
