class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        lower = 0
        upper = rows*cols - 1

        mid = (lower + upper) // 2
        mid_row, mid_col = self.calculateLocation(rows, cols, mid)

        while lower <= upper:
            value = matrix[mid_row][mid_col]
            if value == target:
                return True

            if value < target:
                lower = mid + 1
            elif value > target:
                upper = mid - 1
            
            mid = (lower + upper) // 2
            mid_row, mid_col = self.calculateLocation(rows, cols, mid)
        return False
    
    def calculateLocation(self, rows, cols, index) -> []:
        # return row, col
        row = index // cols
        col = index % cols
        return [row, col]
