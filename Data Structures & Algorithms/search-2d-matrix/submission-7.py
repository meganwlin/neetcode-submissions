class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        min = 0
        max = rows * cols - 1

        while min <= max:
            index = min + (max - min)//2
            r, c = self.calculateRowCol(rows, cols, index)
            if matrix[r][c] < target:
                min = index + 1
            elif matrix[r][c] > target:
                max = index - 1
            else:
                return True
        return False



    def calculateRowCol(self, rows, cols, index):
        r = index // cols
        c = index % cols
        return r,c
        