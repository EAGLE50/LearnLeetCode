# -*- coding:utf-8 -*-
# @Time : 2020/6/18 20:58 
# @Author : bendan50
# @File : Q19-remove-nth-from-end.py
# @Function : 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
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
    思路：保持相同间隔。既然想删除倒数第N个，可以先从头遍历到从头开始的第N个，然后“头尾”依次向后至链表尾。
    注意：在找到从头起第N+1时，要先判断空，再依次next向后。
    N+1的原因是链表的删除，需要知道被删除点的前结点。
    """
    def removeNthFromEnd(self, head, n):
        del_node = tail = head
        while tail and n > 0:
            tail = tail.next
            n -= 1
        # 此处必须先判空
        if not tail:
            head = head.next
            del del_node
            return head
        while tail.next:
            tail = tail.next
            del_node = del_node.next
        print('tail.val = {}'.format(tail.val))
        print('del_node.val = {}'.format(del_node.val))
        temp = del_node.next
        del_node.next = temp.next
        del temp
        return head


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
    # l = create_list_for_test([1,2,3,4,5])
    l = create_list_for_test([5])
    ret = Solution().removeNthFromEnd(l,1)
    if ret:
        ret.print_node()
    else:
        print(ret)