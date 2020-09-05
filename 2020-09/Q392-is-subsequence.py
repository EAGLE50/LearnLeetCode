# -*- coding:utf-8 -*-
# @Time : 2020/9/4 21:46 
# @Author : bendan50
# @File : Q392-is-subsequence.py 
# @Function : 判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
# （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 示例 1:
# s = "abc", t = "ahbgdc"
# 返回 true.
# 示例 2:
# s = "axc", t = "ahbgdc"
# 返回 false.
# 后续挑战 :
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
# @Software: PyCharm

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        思路：使用双指针方法，但贪心算法如何体现呢？
        遍历子序列，当找到第一个与s[i]相等的字符，则从t[j]的位置继续找s[i+1]字符
        当子序列遍历完，则返回True；若序列t先结束，则说明未找到子序列中的字符，返回 False
        :param s:
        :param t:
        :return:
        """
        s_size = len(s)
        t_size = len(t)
        j = 0
        for i in range(s_size):
            while j < t_size:
                if s[i] == t[j]:
                    j += 1
                    break
                j += 1
            if j == t_size and i != s_size - 1:     #s未到结尾，t到了结尾
                return False
            if j == t_size and t[j - 1] != s[s_size - 1]:   #s和t都到了结尾，但结尾不相同
                return False
        return True
        pass

    def isSubsequence1(self, s: str, t: str) -> bool:
        """
        官方实现的贪心策略的双指针，太简洁了。学习下。自己太菜，代码写得太low
        :param s:
        :param t:
        :return:
        """
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    def is_Subsequence(self, s: str, t: str) -> bool:
        """
        对于后续挑战的问题，因为k足够大，而双指针的贪心策略花费很长时间在遍历t
        当k足够大时，会出现反复遍历相同t，所以出发点很简单，在遍历k条s时，需要遍历一次t
        仅且遍历一次，后续直接使用，问题变成单纯遍历k条s了。因为要处理k条s，所以这个遍历是必须且必要的。
        问题转化为：如何遍历常数次t，将接下来匹配s所需要的信息记录下来呢？
        回答：动态规划！
        第二个问题：记录什么信息，怎么记录？约等于回答：数组存储的值具有什么含义，状态转换方程如何表示？
        令f[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。
        f[i][j]是一个行为len(t)，列为26，表示可能出现的26个小写字母。
        如果 t 中位置 i 的字符就是 j，那么 f[i][j]=i，
        否则 j 出现在位置 i+1 开始往后，即 f[i][j]=f[i+1][j]
        突然发现转换过程是从后往前的，即需要先知道最后一行。所以！！！
        f[i][j]改为len(t)+1行，最后一行存储len(t)的值，含义是字符j不在从i往后的字符里
        即：如果 f[i][j]=len(t)，则表示从位置 i 开始往后不存在字符 j
        :param s:
        :param t:
        :return:
        """
        s_size,m_size = len(s),len(t)
        f = [[0]*26 for _ in range(m_size)]
        f.append([m_size]*26)   #添加最后一行
        #初始化f[i][j]之后，开始定义状态转换
        for i in range(m_size - 1, -1, -1): #[m_size-1,0]的遍历
            for j in range(26):
                if ord(t[i]) - ord('a')  == j:
                    f[i][j] = i
                else:
                    f[i][j] = f[i+1][j]
        #预处理结束
        row = 0     #开始的行，从f[i][j]第0行开始。
        for i in range(s_size):
            col = ord(s[i]) - ord('a')
            if f[row][col] == m_size:
                return False
            else:
                row = f[row][col] + 1
        return True