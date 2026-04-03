# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linked_list = []

        for node in lists:
            while node:
                linked_list.append(node.val)
                node = node.next

        linked_list.sort()
        dummy = cur = ListNode()

        for val in linked_list:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
