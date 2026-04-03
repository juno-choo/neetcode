# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxV):
            if not node:
                return 0

            res = 1 if node.val >= maxV else 0
            return res + dfs(node.left, max(maxV, node.val)) + dfs(node.right, max(maxV, node.val))

        return dfs(root, root.val)    
            