class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # # inorder traversal
        # # arr = [1, 3, 2, 4]
        #            m1  m2

        # # arr = [1, 4, 3, 2, 5]
        #             m1    m2   

        m1 = None
        m2 = None
        prev = None

        found = False
        def inorder(node):
            nonlocal m1
            nonlocal m2
            nonlocal prev
            nonlocal found

            if not node:
                return

            inorder(node.left)
            if prev and node.val < prev.val:
                if found:
                    m2 = node
                else:
                    m1 = prev
                    m2 = node
                    found = True
            prev = node
            inorder(node.right)

        inorder(root)

        m1.val, m2.val = m2.val, m1.val
# m1 = 3, m2 = 2
        return