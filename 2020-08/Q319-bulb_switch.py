# -*- coding:utf-8 -*-
# @Time : 2020/8/3 19:01 
# @Author : bendan50
# @File : Q319-bulb_switch.py
# @Function : 灯泡开关
# 初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。
# 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。
# 第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。
# 找出 n 轮后有多少个亮着的灯泡。
# 示例:
# 输入: 3
# 输出: 1
# 解释:
# 初始时, 灯泡状态 [关闭, 关闭, 关闭].
# 第一轮后, 灯泡状态 [开启, 开启, 开启].
# 第二轮后, 灯泡状态 [开启, 关闭, 开启].
# 第三轮后, 灯泡状态 [开启, 关闭, 关闭].
# 你应该返回 1，因为只有一个灯泡还亮着。
# @Software: PyCharm

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        思路：首先，这一定是一个不可取的方法！创建个数组，模拟灯泡。然后从头遍历n次，每次步幅为n
        :param n:
        :return:
        """
        flag = []
        for i in range(n):
            flag.append(False)
        count = 1
        while count <= n:
            idx = count
            while idx <= n:
                flag[idx - 1] = not flag[idx - 1]
                idx += count
            print('{} - {}'.format(count, flag))
            count += 1
        pass
        num = 0
        for _, ele in enumerate(flag):
            if ele:
                num += 1
        return num

    def func2(self, n):
        """
        思路：发现灯泡的被操作次数与这个数的因子个数有关。
        比如12这个灯泡，当count=1、2、3、4、6、12时都将影响这个灯泡，它的最终结果是关！因为因子个数是偶数
        所以一次遍历即可，且不需要额外的存储空间。
        很抱歉地通知：时间超出限制，在求因子的时间，方法依然不可取！！！
        :param n:
        :return:
        """
        pass
        ret = 0
        for i in range(1, n + 1, 1):
            num = self.factor_num(i)
            if num % 2 == 1:
                ret += 1
        return ret

    def factor_num(self, ele):
        """
        求ele的因子个数
        :param ele:
        :return:
        """
        ret = 1  # 已经将ele自身算进去了。
        for i in range(1, ele):
            if ele % i == 0:
                ret += 1
        return ret

    def bulb_switch(self, n: int) -> int:
        """
        完美的解法！！
        我们一路实验过来，最后的问题转变成什么了？1--n中因子个数是奇数的数字个数！
        对，求所谓的因子个数，仅仅是为了判断个数是奇是偶，那么可不可以不需要遍历就知道呢？
        设 x = a*b 若不存在a=b的情况，则x的因子个数一定为偶数；
        若存在a=b的情况，则x的因子个数一定为奇数。
        问题解决了。
        :param n:
        :return:
        """
        ret = 1
        while ret * ret <= n:
            ret += 1
        return ret-1        #因为while里面多加了一次，不符合条件，才退出的。


if __name__ == "__main__":
    n = 10
    ret = Solution().func(n)
    ret2 = Solution().func2(n)
    print('ret = {}'.format(ret))
    print('ret2 = {}'.format(ret2))
