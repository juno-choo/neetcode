# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0] 
        result = [None] 

        def dfs(node):
            if not node or result[0] is not None:
                # Add a check here to stop the recursion early 
                # if we have already found the result!
                return
            
            # 1. Traverse Left
            dfs(node.left)
            # 2. Process Current Node: Update count, Check if count == k
            count[0] += 1
            if count[0] == k: 
                result[0] = node.val
                return 
            # 3. Traverse Right
            dfs(node.right)

        dfs(root)
        return result[0]