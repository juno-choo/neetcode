# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        # Move prev right before start of range
        for _ in range(left - 1):
            prev = prev.next

        # Save cur (pointer will persist)
        tail = prev
        cur = prev.next
        prev = None

        # Move right - left steps while reversing 
        for _ in range(right - left + 1):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        tail.next.next = cur
        tail.next = prev
            
        return dummy.next