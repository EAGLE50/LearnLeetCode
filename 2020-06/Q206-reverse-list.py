# -*- coding:utf-8 -*-
# @Time : 2020/6/22 22:00 
# @Author : bendan50
# @File : Q206-reverse-list.py 
# @Function : 反转一个单链表。
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        思路：完全就是一个链表遍历与在链表头部插入元素的基本操作。
        :param head:
        :return:
        """
        if not head:
            return head
        h = ListNode(-1)    #临时头结点
        while head:
            temp = head
            head = head.next
            temp.next = h.next
            h.next = temp
        ret = h.next
        h.next=None
        del h
        return ret

    def reverse_list(self, head: ListNode) -> ListNode:
        """
        官方迭代方法：不推荐。思路：记录前中后三个结点
        :param head:
        :return:
        """
        if not head:
            return head
        pre_node = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return pre_node