# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        dummy = root
        stack = [root]
        while stack:
            head = stack.pop()
            if head.left:
                stack.append(head.left)
            if head.right:
                stack.append(head.right)
            head.left, head.right = head.right, head.left
            
        return dummy
            


        
