class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(r, c ,area):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return area

            area += 1
            grid[r][c] = 0

            max_area = area
            for dr, dc in directions:
                area = max(area, dfs(r + dr, c + dc, area))
            return area
        
        max_island = 0
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    area = dfs(r, c, 0)
                    max_island = max(area, max_island)
        return max_island



        