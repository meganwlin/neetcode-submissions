# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = [root]

        while q:
            head = q.pop(0)
            left = head.left
            right = head.right

            head.right = left
            head.left = right

            if right:
                q.append(right)
            if left:
                q.append(left)
        return root

        
