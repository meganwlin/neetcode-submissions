# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        answer = head
        if head.next:
            answer = self.reverseList(head.next) # moves it to the end
            future = head.next
            future.next = head # swapping here
        # Finished swapping, so we set the first node's next to None
        head.next = None
        return answer
        
        


