class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        l, r = 0, (rows * cols) - 1

        while l <= r:
            index = (l+r)//2
            row = index // cols
            col = index % cols
            val = matrix[row][col]


            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = index + 1
            else:
                r = index - 1
        return False