# -*- coding:utf-8 -*-
# @Time : 2020/8/22 17:41 
# @Author : bendan50
# @File : Q1227_nth_person_gets_nth_seat.py 
# @Function : 飞机座位分配概率
# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
# 剩下的乘客将会：
# 如果他们自己的座位还空着，就坐到自己的座位上，
# 当他们自己的座位被占用时，随机选择其他座位
# 第 n 位乘客坐在自己的座位上的概率是多少？
# 示例 1：
# 输入：n = 1
# 输出：1.00000
# 解释：第一个人只会坐在自己的位置上。
# 示例 2：
# 输入: n = 2
# 输出: 0.50000
# 解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
# @Software: PyCharm

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        思路：很简单的，是一个递归问题。设f(n-1) = x,则f(n) = 1/n + (n-2)/n*f(n-1)
        含义就是第一个客人，正好坐在了他的位置上，即为1/n
        若第一个客人，没有坐在他的位置且没坐在第n个人的位置上，概率为(n-2)/n，问题转为n-1个人第n-1个人坐在自己座位的概率
        官方：给出公式推理与化解，得出当n>=2时，f(n)=0.5，即恒等于0.5
        所以，也就一行代码 return 1 if n == 1 else 0.5
        :param n:
        :return:
        """
        # 使用递归实现
        if n == 1:
            return 1.0
        if n == 2:
            return 1.0 / n
        return 1.0 / n + (n - 2) * 1.0 / n * self.nthPersonGetsNthSeat(n - 1)
        pass

if __name__ =="__main__":
    ret = Solution().nthPersonGetsNthSeat(3)
    print('ret = {}'.format(ret))