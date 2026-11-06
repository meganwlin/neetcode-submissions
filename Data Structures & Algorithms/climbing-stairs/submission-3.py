class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                return dfs(n-1) + dfs(n-2)
        return dfs(n)