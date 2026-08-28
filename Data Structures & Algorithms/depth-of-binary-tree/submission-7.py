# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = -1

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                q.append(node.left) if node else None
                q.append(node.right) if node else None
            res += 1

        return res



