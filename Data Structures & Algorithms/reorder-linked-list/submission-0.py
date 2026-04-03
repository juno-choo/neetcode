# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find middle node of LL
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse LL from middle to end
        curr = slow
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #Merge alternate nodes from head and reversed LL respectively
        head1 = head
        head2 = prev

        while head2.next:
            tmp = head1.next
            head1.next = head2
            head1 = tmp
            tmp = head2.next
            head2.next = head1
            head2 = tmp 



        