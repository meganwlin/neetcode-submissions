class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                memo[i] = 1
                return 1
            if i > n:
                memo[i] = 0
                return 0
            else:
                answer = dfs(i+1) + dfs(i+2)
                memo[i] = answer
                return memo[i]
        return dfs(0)