class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            q = deque()
            q.append([i, j])
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while q:
                x, y = q.pop()
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                elif grid[x][y] == "0":
                    continue
                else:
                    grid[x][y] = "0"
                    for dx, dy in dirs:
                        q.append([dx + x, dy + y])
        
        num = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    bfs(x, y)
                    num += 1
        return num