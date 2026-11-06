class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            # is not in bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0

            # is water
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            total  = 0
            for dr, dc in dirs:
                total += dfs(r + dr, c + dc)

            # mark current space as part of island (+1) and continue search in all directiokns
            return 1 + total
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
