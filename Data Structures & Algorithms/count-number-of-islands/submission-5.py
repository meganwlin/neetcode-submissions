class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            
            # set current space to water
            grid[r][c] = "0"

            # traverse in all directions
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return
        
        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print(f"Row {r}, Col {c} : {grid[r][c]}")
                if grid[r][c] == "1":
                    dfs(r, c)
                    counter += 1
        return counter
            