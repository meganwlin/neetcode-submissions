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
        queue = [root]
        dummy = root

        while queue:
            head = queue.pop(0)
            head.left, head.right = head.right, head.left
            if head.right:
                queue.append(head.right)
            if head.left:
                queue.append(head.left)
            
        return dummy
            


        
