class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if memo[i] != -1:
                print(f"{i} already has a value of {memo[i]}")
                return memo[i]

            total = dfs(i+1)+ dfs(i+2)
            memo[i] = total
            return total
        return dfs(0)
