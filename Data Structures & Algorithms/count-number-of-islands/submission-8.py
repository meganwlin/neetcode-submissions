class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i == len(grid) or j <0 or j == len(grid[0]):
                return
            if grid[i][j] == "0":
                return 
            grid[i][j] = "0" # flip it to water so we don't double count
            # up , down , left, right
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            return
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands

            