# -*- coding:utf-8 -*-
# @Time : 2020/6/20 20:40 
# @Author : bendan50
# @File : Q138-copy-random-list.py 
# @Function :
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的 深拷贝。
# @Software: PyCharm


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    思路一：使用深度优先搜索思想，递归（回溯）创建链表，太难了，转不明白。
    思路二：两次遍历，第一次处理next结点，并创建字典；第二次处理random结点。原链表结点是key,顺序n是value。
            这样第二次遍历原链表时，直接就可以知道，random指向第几个结点(n的值)，所以新链表的字典key是顺序n，结点是vaule
            采用此思路通过全部用例。空间复杂度O(n)
    思路三：官方解析给出。之前未想到。空间复杂度O(1)。思路二的优化版本，也是分两次分别处理next和random结点，但不需要字典
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        print('hello world = {}'.format(head))
        old_node_hash = {}  # 创建一字典，key是链表的结点，value是链表的顺序n
        new_node_hash = {}  #存储新建的结点，key是链表的顺序n，value是这个链表中的第n个结点
        if not head:
            return head
        copy_list = tail = Node(-1) #临时头节点
        h1 = head
        idx = 0
        while h1:
            node = Node(h1.val)
            tail.next = node
            old_node_hash.__setitem__(h1,idx)
            new_node_hash.__setitem__(idx,node)
            h1 = h1.next
            tail = node
            idx += 1
        h2 = head
        t = copy_list.next
        while h2:
            if h2.random:
                node_id = old_node_hash.get(h2.random)
                t.random = new_node_hash.get(node_id)
            t = t.next
            h2 = h2.next
        ret = copy_list.next
        del copy_list
        return ret


    def copy_random_list(self,head: 'Node')->'Node':
        """
        思路三的实现。
        :param head:
        :return:
        """
        if not head:
            return head
        h1 = head
        while h1:
            # 新建结点，并插入原链表所拷贝结点的后面，新旧交替的结点顺序
            node = Node(h1.val)
            node.next = h1.next
            h1.next = node
            h1 = h1.next.next
        h2 = head
        while h2:
            copy_node = h2.next
            # 注意空指针
            if h2.random:
                copy_node.random = h2.random.next
            h2 = h2.next.next
        # 分离出新链表
        ret = tail = head.next
        while tail:
            if tail.next:
                tail.next = tail.next.next
            tail = tail.next
        return ret


if __name__ == '__main__':
    Solution().copyRandomList(None)
