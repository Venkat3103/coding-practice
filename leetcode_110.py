# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            #print(node)
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Check if the subtree is balanced and calculate the height
            #print("For ",node.val," left height: ", left_height)
            #print("For ",node.val," right height: ", right_height)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            print(node.val,left_height,right_height)
            return 1 + max(left_height, right_height)
        return height(root) != -1

#https://leetcode.com/problems/balanced-binary-tree/description/