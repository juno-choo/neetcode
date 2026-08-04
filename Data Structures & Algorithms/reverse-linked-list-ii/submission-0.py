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
        cur = prev.next

        # Move right - left steps while reversing 
        for _ in range(right - left):
            nextNode = cur.next
            cur.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode

        return dummy.next