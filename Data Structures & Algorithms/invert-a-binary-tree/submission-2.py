# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeUsingBFS(root)
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
    
    def invertTreeUsingBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]
        temp = []

        while stack or temp:
            while stack:
                node = stack.pop()
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
                left = node.left
                right = node.right

                node.left = right
                node.right = left

            stack = temp
            temp = []
        return root
            

        

        