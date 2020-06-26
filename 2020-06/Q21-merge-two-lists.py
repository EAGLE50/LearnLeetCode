# -*- coding:utf-8 -*-
# @Time : 2020/6/24 21:52 
# @Author : bendan50
# @File : Q21-merge-two-lists.py 
# @Function : 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        思路：新建一个临时头结点，从头开始依次比较两个链表的结点，最小的结点插入到新链表后面。
        结果：迭代。
        :param l1:
        :param l2:
        :return:
        """
        head = tail = ListNode(-1)  # 临时头结点
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        ret = head.next
        head.next = None
        del head
        return ret
