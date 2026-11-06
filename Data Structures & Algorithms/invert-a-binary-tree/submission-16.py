# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()

        head = root

        q.append(root)
        if not root:
            return root

        while q:
            top = q.popleft()
            # if not top: continue
            l, r = top.left, top.right
            top.right = l
            top.left = r

            if l:
                q.append(l)
            if r:
                q.append(r)
        return head
        