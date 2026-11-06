# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeUsingBfsQueue(root)
        return root
        
    def invertTreeUsingDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left = root.left
        right = root.right

        self.invertTreeUsingDFS(root.left)
        self.invertTreeUsingDFS(root.right)

        root.right = left
        root.left = right

        return root
    
    def invertTreeUsingDFSStack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            left = node.left
            right = node.right

            node.left = right
            node.right = left
        return root
    
    def invertTreeUsingBfsQueue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = [root]

        while q:
            node = q.pop(0)
            left = node.left
            right = node.right

            node.left = right
            node.right = left

            if right:
                q.append(right)
            if left:
                q.append(left)
        return root

            

        

        