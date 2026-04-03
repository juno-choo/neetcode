class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_range, r_range = 0, len(matrix) - 1
        while l_range <= r_range:
            mid_range = (r_range + l_range) // 2

            l, r = 0, len(matrix[0]) - 1
            if matrix[mid_range][l] <= target <= matrix[mid_range][r]:       
                while l <= r:
                    m = (l+r) // 2
                    if matrix[mid_range][m] == target:
                        return True
                    elif matrix[mid_range][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False

            elif target > matrix[mid_range][r]:
                l_range = mid_range + 1
            else:
                r_range = mid_range - 1

        return False
            