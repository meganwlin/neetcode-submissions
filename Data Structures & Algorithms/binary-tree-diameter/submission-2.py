# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.dfs(root.left)
        rightDepth = self.dfs(root.right)
        # make current node the midpoint
        current = leftDepth + rightDepth

        # go down the tree to make each node the midpoint, and recalculate
        return max(current, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))


    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))