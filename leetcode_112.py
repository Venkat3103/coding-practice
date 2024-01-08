# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,targetSum):
            if not node:
                return False
            targetSum -= node.val
            if targetSum==0 and node.right==None and node.left==None:
                return True
            return dfs(node.right,targetSum) or dfs(node.left,targetSum)
        return dfs(root,targetSum)

#https://leetcode.com/problems/path-sum/description/