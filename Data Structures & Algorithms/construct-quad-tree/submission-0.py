"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            # Iterate over grid to prune 
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            
            # This can be a leaf node
            if allSame:        
                return Node(grid[r][c], 1)

            # Formula to recurse
            n //= 2

            # Assign children
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            return Node(grid[r][c], 0, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)
