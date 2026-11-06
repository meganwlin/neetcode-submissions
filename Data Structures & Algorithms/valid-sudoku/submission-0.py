class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [set() for i in range(9)]
        col_seen = [set() for i in range(9)]
        box_seen = [set() for i in range(9)]

        for i in range(9): # row index
            for j in range(9): # column index
                num = board[i][j]

                if num == ".":
                    continue

                if num in row_seen[i]:
                    return False
                else:
                    row_seen[i].add(num)

                if num in col_seen[j]:
                    return False
                else:
                    col_seen[j].add(num)
                
                box_number = ((i//3)) * 3 + (j//3)
                if num in box_seen[box_number]:
                    return False
                else:
                    box_seen[box_number].add(num)
        return True