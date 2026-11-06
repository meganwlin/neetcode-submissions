class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0 # flip it so we don't come back to this spot
                up = dfs(i, j-1)
                down = dfs(i, j+1)
                left = dfs(i-1, j)
                right = dfs(i+1, j)
                return 1 + up + down + left + right
            return 0
        
        maxIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxIslands = max(dfs(i, j), maxIslands)
        return maxIslands
