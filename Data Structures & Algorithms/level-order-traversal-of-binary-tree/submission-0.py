# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        heights = []

        h = 0
        while q:
            width = len(q)
            nodes_at_height = []
            
            next_level = []
            for node in q:
                nodes_at_height.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if nodes_at_height:
                heights.append(nodes_at_height)
            q = next_level
        return heights
            





        
