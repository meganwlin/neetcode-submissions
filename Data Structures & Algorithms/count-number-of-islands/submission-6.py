class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dx, dy in dirs:
                dfs(i+dx, j+dy)
            return
        
        num = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    num += 1
        return num