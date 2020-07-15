# -*- coding:utf-8 -*-
# @Time : 2020/7/12 21:44 
# @Author : bendan50
# @File : Q6-convert.py 
# @Function : Z 字形变换
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# @Software: PyCharm

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        思路：写代码模拟下这个Z字的排列，很容易想到的是二维数组，行数由min(numRows,len(s))决定。
        然后一个遍历s，一个指针在行数组之间切换，根据方向，然后就是把遍历的字符添加到对应的行数组里
        分为两步：第一步改变方向，第二步，改变下标
        :param s:
        :param numRows:
        :return:
        """
        rows = min(numRows, len(s))
        if rows <= 1:
            return s
        ret = [[] for i in range(rows)]  # python创建二维数组
        print(ret)
        row_idx = 0
        going_down = False
        for idx, ele in enumerate(s):
            ret[row_idx].append(ele)
            if row_idx == 0 or row_idx==rows-1:
                going_down = not going_down     #取反
            if going_down:
                row_idx += 1
            else:
                row_idx -= 1
        result = ""
        for i in range(rows):
            result = result + "".join(ret[i])
        return result


if __name__ == "__main__":
    ret = Solution().convert('LEETCODEISHIRING', 3)
    print('ret = {}'.format(ret))


# class Solution {
# public:
#     string convert(string s, int numRows) {
#
#         if (numRows == 1) return s;
#
#         vector<string> rows(min(numRows, int(s.size())));
#         int curRow = 0;
#         bool goingDown = false;
#
#         for (char c : s) {
#             rows[curRow] += c;
#             if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
#             curRow += goingDown ? 1 : -1;
#         }
#
#         string ret;
#         for (string row : rows) ret += row;
#         return ret;
#     }
# };

