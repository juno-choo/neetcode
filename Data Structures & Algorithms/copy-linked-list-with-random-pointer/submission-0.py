"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {None : None}
        cur = head
        while cur:
            visited[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            visited[cur].next = visited[cur.next]
            visited[cur].random = visited[cur.random]
            cur = cur.next

        return visited[head]

