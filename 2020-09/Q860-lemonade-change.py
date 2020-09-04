# -*- coding:utf-8 -*-
# @Time : 2020/9/3 19:56 
# @Author : bendan50
# @File : Q860-lemonade-change.py 
# @Function : 柠檬水找零
# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
# 你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
# 注意，一开始你手头没有任何零钱。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
# 示例 1：
# 输入：[5,5,5,10,20]
# 输出：true
# 解释：
# 前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
# 第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
# 第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
# 由于所有客户都得到了正确的找零，所以我们输出 true。
# 示例 2：
# 输入：[5,5,10]
# 输出：true
# 示例 3：
# 输入：[10,10]
# 输出：false
# 示例 4：
# 输入：[5,5,10,10,20]
# 输出：false
# 解释：
# 前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
# 对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
# 对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
# 由于不是每位顾客都得到了正确的找零，所以答案是 false。
# 提示：
# 0 <= bills.length <= 10000
# bills[i] 不是 5 就是 10 或是 20 
# @Software: PyCharm

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        思路：这个是非常清晰的贪心算法思路，因为它不需要考虑后面（接下来）可能出现的情况，只需要处理好当前。
        如果不能找零，则直接退出，返回False。
        如果能找零，按最优的方案找零，更新现存的零钱。且找零时，从大面值开始，能找一个10元，不会找两个5元
        :param bills:
        :return:
        """
        have_5 = []
        have_10 = []
        for bill in bills:
            if bill == 5:
                have_5.append(5)
                continue
            elif bill == 10:
                if len(have_5) == 0:
                    return False
                have_5.pop(0)
                have_10.append(10)
            else:       # bill = 20
                if len(have_5) == 0:
                    return False
                elif len(have_10) == 0:
                    if len(have_5) < 3:
                        return False
                    else:
                        have_5.pop(0)
                        have_5.pop(0)
                        have_5.pop(0)
                else:
                    have_10.pop(0)
                    have_5.pop(0)
        return True

if __name__ == "__main__":
    ret = Solution().lemonadeChange([5,5,5,5,20,20,5,5,20,5])
    print('ret = {}'.format(ret))