# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        answer = []

        # Use BFS
        q = deque()
        q.append(root)

        while q:
            node = q.pop() # removes rightmost
            answer.append(node.val)

            next_level = []
            for n in q:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            q = next_level
        return answer

