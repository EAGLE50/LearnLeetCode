# -*- coding:utf-8 -*-
# @Time : 2020/8/31 20:14 
# @Author : bendan50
# @File : Q104-max-depth.py 
# @Function : 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        思路：类似于图的广度搜索，按层遍历。借助于队列的结构。
        :param root:
        :return:
        """
        if root is None:
            return 0
        deep = 1
        queue = []
        queue.append(root)  #0
        queue.append(deep)  #1
        while len(queue) > 0:
            ele = queue.pop(0)
            if type(ele) is TreeNode:
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
            else:
                if len(queue) > 0:
                    ele += 1
                    queue.append(ele)
                else:
                    deep = ele
        return deep

    def max_Depth(self, root: TreeNode) -> int:
        """
        思路：递归，最大层=MAX(左子树层数，右子树层数)+1
        :param root:
        :return:
        """
        if root is None:
            return 0
        return max(self.max_Depth(root.left),self.max_Depth(root.right)) + 1