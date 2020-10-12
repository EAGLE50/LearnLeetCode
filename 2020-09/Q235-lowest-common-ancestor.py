# -*- coding:utf-8 -*-
# @Time : 2020/9/20 15:42 
# @Author : bendan50
# @File : Q235-lowest-common-ancestor.py 
# @Function : 二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
# 最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
# （一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 示例 1:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路：充分利用二叉搜索树的特征：左子树所有值比根值小，右子树所有值比根值大。
        题目已说明，所有节点的值都是唯一。
        找出q/p两个点哪个最大，哪个最小。
        然后不断与根结点判断，当在根结点两边时，当前根结点为最近公共祖先
        当在根结点一边时，更新根结点，即取子树的根结点为新根结点。
        又因为题目已说明,q/p两点均存在于树中
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val == q.val:
            return p
        if p.val < q.val:
            min_v = p
            max_v = q
        else:
            min_v = q
            max_v = p
        tmp = root
        while True:
            if tmp.val == min_v.val or tmp.val == max_v.val:
                return tmp
            elif tmp.val > max_v.val:
                tmp = tmp.left
            elif tmp.val < min_v.val:
                tmp = tmp.right
            else:
                return tmp