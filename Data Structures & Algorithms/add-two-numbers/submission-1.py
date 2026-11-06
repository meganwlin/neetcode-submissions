# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        answer = ListNode()
        head = answer

        while l1 or l2 or overflow:
            total = overflow
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            overflow = total // 10
            print(total%10)
            head.next = ListNode(total % 10)

            head = head.next
        return answer.next

