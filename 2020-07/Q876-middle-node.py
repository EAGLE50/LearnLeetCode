# -*- coding:utf-8 -*-
# @Time : 2020/7/12 16:41 
# @Author : bendan50
# @File : Q876-middle-node.py 
# @Function：链表的中间结点
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        思路：中间点，与链表长度存在两倍的关系。快慢指针，快的一次走两步，保持两倍关系
        :param head:
        :return:
        """
        slow = fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                return slow
            slow = slow.next
        return slow