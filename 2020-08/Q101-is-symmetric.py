# -*- coding:utf-8 -*-
# @Time : 2020/8/22 21:00 
# @Author : bendan50
# @File : Q101-is-symmetric.py 
# @Function : 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# 进阶：
# 你可以运用递归和迭代两种方法解决这个问题吗？
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        思路：对称二叉树的对称轴是根结点，并非每个子树的子根结点，如 [1,2,2,3,4,4,3]的例子。
        所以，只需要以树根结点分别对左子树和右子树遍历即可，结果若相等，则说明对称。
        至于遍历，左子树的顺序是：标准的先序遍历，左中右
        右子树的顺序则是：右中左
        这样的遍历顺序，保证了若遍历结果相等，则说明对称。
        结果：行不通！！！！
        [5,4,1,null,1,null,4,2,null,2,null]
        遍历都是     left = NULL421NULL
                    right = NULL421NULL
        发现了什么呢？首先是根结点相等后，才有比较左右子树的意义。
        所以，遍历顺序改为：中左右   与  中右左
        尝试后通过！
        :param root:
        :return:
        """
        if root is None:
            return True
        left = root.left
        right = root.right
        left_nodes = self.left_mid_right(left)
        right_nodes = self.right_mid_left(right)
        if left_nodes == right_nodes:
            return True
        else:
            return False

    def left_mid_right(self, tree_root: TreeNode):
        if tree_root is None:
            return "NULL"
        if tree_root.left is None and tree_root.right is None:
            return str(tree_root.val)
        return str(tree_root.val) + self.left_mid_right(tree_root.left) + self.left_mid_right(tree_root.right)

    def right_mid_left(self, tree_root: TreeNode):
        if tree_root is None:
            return "NULL"
        if tree_root.left is None and tree_root.right is None:
            return str(tree_root.val)
        return str(tree_root.val) + self.right_mid_left(tree_root.right) + self.right_mid_left(tree_root.left)

    def is_Symmetric(self, root: TreeNode) -> bool:
        """
        递归实现，定义两个指针，一个往左，一个往右,从中心根结点开始
        :param root:
        :return:
        """
        return self.recursive_check(root, root)
        pass

    def recursive_check(self, P1: TreeNode, P2: TreeNode):
        if P1 is None and P2 is None:
            return True
        if P1 is None or P2 is None:
            return False
        return P1.val == P2.val and self.recursive_check(P1.left, P2.right) and self.recursive_check(P1.right,P2.left)
