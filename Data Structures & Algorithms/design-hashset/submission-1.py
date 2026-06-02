"""
The idea is to use chaining where we have array of buckets.
Each bucket is a linked list.
Will need to hash the key (instant) and use the hash as the index for the bucket.
Average time complexity of functions is constant.
Worst case is still linear time.
"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
       self.size = 1000
       self.buckets = [Node() for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key): return

        idx = self.hash(key)

        cur = self.buckets[idx]
        # Traverse LL to find tail
        while cur.next != None:
            cur = cur.next

        # Chain the tail 
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)

        cur = self.buckets[idx]
        # Traverse LL to find node before target node, redirect chain, GC will free node
        while cur.next != None:
            if cur.next.val == key:
                cur.next = cur.next.next if cur.next.next else None
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        idx = self.hash(key)

        cur = self.buckets[idx]
        # Traverse LL to find node with key
        while cur != None:
            if cur.val == key:
                return True
            cur = cur.next
        

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)