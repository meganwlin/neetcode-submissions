# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
        
    def dfs(self, root, maxVal):
        goodNode = 0
        if not root:
            return 0
        if root.val >= maxVal:
            maxVal = root.val
            goodNode = 1
        return goodNode + self.dfs(root.left, maxVal) + self.dfs(root.right, maxVal)