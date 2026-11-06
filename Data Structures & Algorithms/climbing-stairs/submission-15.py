class Solution:
    def climbStairs(self, n: int) -> int:
        # top down
        cache = [-1] * (n+1)

        def dfs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if cache[n] != -1:
                return cache[n]
            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
        return dfs(n)
