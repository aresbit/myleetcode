#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.x = None
        self.y = None
        self.pre = None
        # 中序遍历二叉树，并比较上一个节点(pre)和当前节点的值，如果pre的值大于当前节点值，则记录下这两个节点
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val>root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            dfs(root.right)
        dfs(root)
        # 如果x和y都不为空，说明二叉搜索树出现错误的节点，将其交换
        if self.x and self.y:
            self.x.val,self.y.val = self.y.val,self.x.val


        
# @lc code=end

