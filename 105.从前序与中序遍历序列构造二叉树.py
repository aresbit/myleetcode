#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # build tree use preorder and inorder
        def helper(in_left=0, in_rigth = len(inorder)):
            nonlocal pre_index
            if in_left == in_rigth:
                return None
            root = TreeNode(preorder[pre_index])
            index = inorder.index(preorder[pre_index])
            pre_index += 1
            root.left = helper(in_left, index)
            root.right = helper(index+1, in_rigth)
            return root

        pre_index = 0
        return  helper()

        

# @lc code=end

