# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Store the answer in an empty ListNode
        # Don't check if val is None in ListNodes
        answer = ListNode()
        current = answer # pointer to keep moving
        carryover = 0


        while l1 or l2 or carryover:
            # Calculate the total for this round
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carryover

            # Use math to split the total to fit correct digits
            carryover = total // 10
            current.next = ListNode(total % 10)

            # Move all pointers forward one position
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # move pointer forward one since the first node is empty
        return answer.next

