# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []
        while head.next:
            stack.append(head)
            head = head.next
        
        pointer = head
        while stack:
            next_node = stack.pop()
            pointer.next = next_node
            pointer = pointer.next
        pointer.next = None
        return head
            
