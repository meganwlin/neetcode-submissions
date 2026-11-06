class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row that the target is potentially in (use leftmost element as anchor)
        row_l, row_r = 0, len(matrix) - 1
        while row_l != row_r: # inch down one by one
            left_min = matrix[row_l][0]
            right_min = matrix[row_r][0]

            if left_min == target or right_min == target:
                return True
            elif right_min > target:
                row_r -= 1
            else:
                row_l += 1
        

        # find the target within that row if it exists
        col_l, col_r, = 0, len(matrix[0]) - 1
        while col_l <= col_r:
            col_m = (col_l + col_r) // 2
            val = matrix[row_l][col_m]

            if val == target:
                return True
            elif val < target:
                col_l = col_m + 1
            else:
                col_r = col_m - 1
        return False
