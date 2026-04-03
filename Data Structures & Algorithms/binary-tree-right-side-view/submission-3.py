# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth, res):
            if not node:
                return res
            if len(res) == depth:
                res.append(node.val)
            if node.right:
                dfs(node.right, depth + 1, res)
            if node.left:
                dfs(node.left, depth + 1, res)
            return res
            
        return dfs(root, 0, [])


            