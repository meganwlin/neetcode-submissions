class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0 
        time = 0

        # find all the fresh and rotten fruit
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and q:
            # exit once all fresh fruit are rotten or there are no more rotten fruit left to start from
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        # add it for next round of rotting
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        