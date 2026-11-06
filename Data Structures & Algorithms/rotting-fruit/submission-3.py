class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2: # rotten fruit
                    q.append((i, j)) # add tuple of rotten fruit coordinates
        
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        minute = 0
        while q:
            minute += 1
            count = len(q) # snapshot this
            for n in range(count):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        pass # out of bounds
                    elif grid[nr][nc] == 1: # fresh fruit found
                        freshCount -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                    # else it is an already rotten fruit or is an empty cell
        if freshCount != 0:
            return -1
        return max(0, minute -1)

