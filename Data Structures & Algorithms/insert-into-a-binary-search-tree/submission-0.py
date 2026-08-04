class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return TreeNode(val)

            if node.val < val:
                node.right = dfs(node.right)

            else:
                node.left = dfs(node.left)
            return node

        return dfs(root)