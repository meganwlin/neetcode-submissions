class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0

        def dfs(r, c):
            total = 0
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # within bounds
                if nr in range(len(grid)) and nc in range(len(grid[0])):
                    # new island space
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        total += 1 + dfs(nr, nc)
            return total



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited.add((r,c))
                    area = 1 + dfs(r, c)
                    maxArea = max(maxArea, area)
                else:
                    visited.add((r, c))
        return maxArea
