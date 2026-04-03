class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Make it 1D by converting r pointer to index (m * n) - 1
        l, r = 0, ROWS*COLS - 1
        while l <= r:
            m = (l+r) // 2

            # Find 2D coordinate based on m index
            row, col = m // COLS, m % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        return False

            