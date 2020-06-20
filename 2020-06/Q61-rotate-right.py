# -*- coding:utf-8 -*-
# @Time : 2020/6/18 21:43 
# @Author : bendan50
# @File : Q61-rotate-right.py 
# @Function : 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
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
    思路：不要一次次循环旋转改变链表，相当于循环链表找头、尾结点，然后尾结点的next置空
    第一步：先构建循环链表，第二步：计算第几个节点是新结尾；第三步考虑边界
    """
    def rotate_right(self,head,k):
        # 空链表或只有一个元素或旋转0次
        if not head or not head.next or k == 0:
            return head
        old_tail = tail = head
        list_len = 1
        while old_tail.next:
            old_tail = old_tail.next
            list_len += 1
        print("list_len = {}".format(list_len))
        old_tail.next = head
        #计算实际旋转次数
        step = k % list_len
        pre_order = list_len - step     #从头开始数，第几个结点（从1开始）应该是尾，移动次数需要pre_order-1次
        print("step = {} and pre_order = {}".format(step,pre_order))
        while tail.next and pre_order > 1:
            tail = tail.next
            pre_order -= 1
        ret = tail.next
        tail.next = None
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

if __name__ == "__main__":
    # 样例：1.空集；2.k=0；3.
    # l = create_list_for_test([1,2,3,4,5])
    l = create_list_for_test([0,1,2])
    l.print_node()
    ret = Solution().rotate_right(l,4)
    ret.print_node()