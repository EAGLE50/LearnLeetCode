# -*- coding:utf-8 -*-
# @Time : 2020/7/8 19:11 
# @Author : bendan50
# @File : Q141-has-cycle.py 
# @Function : 环形链表
# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。
# @Software: PyCharm
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        思路：如果是循环链表，以判空为结束条件的话会一直循环无法退出，而且又不知道链表长度。
            我们希望，结束条件为相同节点，比如next的结点已经访问过了，说明有循环。此时需要将每个访问过的结点记录下来。
            基于这个思路，空间复杂度是O(n)，问题是还可以改进吗？
        改进：见has_cycle()函数
        :param head:
        :return:
        """
        pos = 0
        p = head
        ps = {}
        idx = 0
        while p:
            if p in ps:
                pos = ps.get(p)
                print('pos = {}'.format(pos))
                return True
            else:
                ps.__setitem__(p,idx)
            p = p.next
            idx += 1
        return False

    def has_cycle(self, head: ListNode) -> bool:
        """
        思路：在空间复杂度为O(1)的前提下，解决该问题。那么如何去表示节点已经访问过呢？
            想想高中运动会的长跑，套圈了！一个快，一个慢，要么快的先到终于，两者没有交点；要么快的赶上慢的，两者有交点
        :param head:
        :return:
        """
        slow = head
        if not head:
            return False
        fast = head.next
        while fast:
            if slow == fast:
                return True
            if not fast.next:
                return False
            slow = slow.next    #慢的一次一个结点
            fast = fast.next.next   #快的一次两个结点
        return False