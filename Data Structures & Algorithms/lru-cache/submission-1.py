class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = ListNode(), ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        left, right = self.right.prev, self.right
        left.next, right.prev = node, node
        node.prev, node.next = left, right


    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove lru
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
