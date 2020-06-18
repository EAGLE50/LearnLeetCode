# -*- coding:utf-8 -*-
# @Time : 2020/6/18 19:29 
# @Author : bendan50
# @File : Q2-add-two-numbers.py 
# @Function : 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
# 并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_node(self):
        t = self
        while t:
            print("{}".format(t.val),end=' -> ')
            t = t.next
        print()

class Solution:
    """
    思路：链表已经是逆序的了，按小学加法逐位计算即可。
    第一步：设初始进位0，然后逐位和进位相加。
    第二步：考虑一个链表为空；考虑两个链表都为空时且有进位。
    """
    def addTwoNumbers(self, l1, l2):
        ret = tail = ListNode(-1)
        temp = 0
        while l1 and l2:
            val = (l1.val + l2.val + temp) % 10
            temp = (l1.val + l2.val + temp) // 10
            if tail.val == -1:
                ret.val = tail.val = val
            else:
                node = ListNode(val)
                tail.next = node
                tail = node
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = (l1.val + temp) % 10
            temp = (l1.val + temp) // 10
            node = ListNode(val)
            tail.next = node
            tail = node
            l1 = l1.next
        while l2:
            val = (l2.val + temp) % 10
            temp = (l2.val + temp) // 10
            node = ListNode(val)
            tail.next = node
            tail = node
            l2 = l2.next
        if temp > 0:
            node = ListNode(temp)
            tail.next = node
        return ret


def create_list_for_test(list):
    head = tail = ListNode(-1)
    for val in list:
        node = ListNode(val)
        if tail.val == -1:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


if __name__ == '__main__':
    l1 = create_list_for_test([2,4,3])
    l2 = create_list_for_test([5,6,4])
    l1 = create_list_for_test([5])
    l2 = create_list_for_test([5])
    ret = Solution().addTwoNumbers(l1,l2)
    ret.print_node()