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
        
        current = self.treeHeight(root.left) + self.treeHeight(root.right)
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return max(current, left, right)

        
    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))