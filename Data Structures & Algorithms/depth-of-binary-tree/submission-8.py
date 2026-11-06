# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if not root:
            return 0

        q.append([root, 1])
        maxLevel = 1

        while q:
            node, level = q.popleft()
            l, r = node.left, node.right
            if l:
                q.append([l, level+1])
            if r:
                q.append([r, level+1])
            maxLevel = max(level, maxLevel)
        return maxLevel

        