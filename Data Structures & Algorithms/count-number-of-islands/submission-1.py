class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # mark as seen
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # every point is a starting point, but board is updated with every search
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
            

        