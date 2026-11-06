class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dir_r, dir_c in directions:
                new_r = r + dir_r
                new_c = c + dir_c
                if new_r in range(0,rows) and new_c in range(0, cols):
                    if grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        bfs(new_r, new_c)

        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands
        