class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dir_r, dir_c in directions:
                    new_r = r + dir_r
                    new_c = c + dir_c
                    if new_r in range(0,rows) and new_c in range(0, cols):
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 0
                            q.append((new_r, new_c))
                            area += 1
            return area

        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == 1:
                    maxIslandArea = max(maxIslandArea, bfs(r, c))
        return maxIslandArea