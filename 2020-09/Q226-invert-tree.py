# -*- coding:utf-8 -*-
# @Time : 2020/9/20 15:23 
# @Author : bendan50
# @File : Q226-invert-tree.py 
# @Function : 翻转二叉树
# 示例：
# 输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        思路：第一想法就是递归，翻转的定义就是互换左右子树的位置，子树作为根树也需要翻转
        :param root:
        :return:
        """
        pass
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root