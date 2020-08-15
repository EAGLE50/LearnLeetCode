# -*- coding:utf-8 -*-
# @Time : 2020/7/16 20:46 
# @Author : bendan50
# @File : Q155-min-stack.py 
# @Function : 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 提示：
# pop、top 和 getMin 操作总是在 非空栈 上调用。
# @Software: PyCharm

class MinStack:
    """
    思路：入栈值与栈顶元素比较，当小于栈顶元素所对应的最小值时，则更新最小值，否则沿用之前的最小值。
    相当于维护了一个最小值的帧。空间复杂度O(n)，不推荐
    改进：可否实现空间复杂度O(1)呢？
    查阅了解析(https://zhuanlan.zhihu.com/p/87257507)，方案是：栈里存在差值（x-min）
    当差值小于0时，则更新min；否则最小值不变。
    该方法（存差值）有前提，数值范围限制。显然这道题的O(1)空间复杂度不可行。
    """

    def __int__(self):
        self.stack = []
        self.min = []
        self.size = 0

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min.append(x)
            self.size += 1
        else:
            top = self.min[self.size - 1]
            self.stack.append(x)
            self.min.append(x if x < top else top)
            self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min[self.size - 1]

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min = 0
    #
    # def push(self, x: int) -> None:
    #     if len(self.stack) == 0:  # 空栈
    #         self.stack.append(0)
    #         self.min = x
    #     else:
    #         temp = x - self.min
    #         self.stack.append(temp)
    #         self.min = x if temp < 0 else self.min
    #
    # def pop(self) -> None:
    #     top = self.stack[len(self.stack) - 1]
    #     self.min = self.min - top if top < 0 else self.min
    #     self.stack.pop()
    #
    # def top(self) -> int:
    #     top = self.stack[len(self.stack) - 1]
    #     return top if top < 0 else top + self.min
    #
    # def getMin(self) -> int:
    #     return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
