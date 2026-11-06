class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    q.append((i, j))
                
                while q:
                    land = q.popleft()
                    x, y = land[0], land[1]

                    if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]): # OOB
                        continue
                    elif grid[x][y] == "0": # water
                        continue
                    else:
                        grid[x][y] = "0" # flip it to water
                        q.append((x+1, y))
                        q.append((x-1, y))
                        q.append((x, y-1))
                        q.append((x, y+1))
                    
        return islands

            