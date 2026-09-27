# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # have global var for max_path_sum
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.res = max(self.res, left + right + node.val)
            return max(left + node.val, right + node.val)
            
        dfs(root)
        return self.res