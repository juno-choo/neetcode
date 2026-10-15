# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            cur = prev
            for _ in range(k): # move k times
                if cur.next:
                    cur = cur.next
                else:
                    return dummy.next

            node = prev.next # first node to reverse
            nextGroup = cur.next
            reversePrev = None
            
            for _ in range(k): # reversal
                nextNode = node.next
                node.next = reversePrev
                reversePrev = node
                node = nextNode

            tail = prev.next # points to first node before reversal
            prev.next = reversePrev # connects prev group to reversed group head
            tail.next = nextGroup # connects reversed tail to next group
            prev = tail # prev is now the end of prev group