class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            if grid[r][c] == "0":
                # stop when you find water
                return
            grid[r][c] = "0"
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]
                if new_r >= 0 and new_r < len(grid) and new_c >=0 and new_c < len(grid[0]):
                    dfs(new_r, new_c)
            return
        num = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num += 1
                    dfs(r, c)
        return num
        