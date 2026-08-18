class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowFlag, colFlag = False, False
        ROWS, COLS = len(matrix), len(matrix[0])

        # Find zeroes and set [row][0] and [0][col] to 0 as marker 
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0:
                        rowFlag = True
                    if col == 0:
                        colFlag = True

                    elif row != 0 and col != 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        # Set inner elements to zero
        for row in range(1, ROWS):
            for col in range(1, COLS):
                # Based on marker
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # Set 1st row and/or col to 0 if flag is set
        if rowFlag:
            for c in range(COLS):
                matrix[0][c] = 0
        if colFlag:
            for r in range(ROWS):
                matrix[r][0] = 0