#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# type 'a tree = Nil | Node of 'a tree * 'a * 'a tree
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #max path sum
        # ans = float('-inf')
        # def dfs(node):
        #     nonlocal ans
        #     if not node:
        #         return 0
        #     left = max(dfs(node.left), 0)
        #     right = max(dfs(node.right), 0)
        #     ans = max(ans, left + right + node.val)
        #     return max(left, right) + node.val
        # dfs(root)
        # return ans
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            ans = max(ans, left + right + node.val)
            return max(left, right) + node.val
        dfs(root)
        return ans



# @lc code=end

