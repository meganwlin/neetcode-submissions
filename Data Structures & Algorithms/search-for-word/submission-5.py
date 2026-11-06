class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, idx):
            if board[r][c] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            # mark current char as visited for this current search
            og = board[r][c]
            board[r][c] = "0"
            
            dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
            for dir_r, dir_c in dirs:
                new_r, new_c = r + dir_r, c + dir_c
                if new_r >= 0 and new_r < len(board) and new_c >= 0 and new_c < len(board[0]):
                    if dfs(new_r, new_c, idx + 1):
                        return True
            board[r][c] = og
            return False

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False

        