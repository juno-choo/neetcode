class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [Node() for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # Find hash idx
        idx = self.hash(key)
        # Need to find if key already exists, if it does, replace the val
        cur = self.buckets[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # IF not, create a new node
        cur.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        cur = self.buckets[idx]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        cur = self.buckets[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)