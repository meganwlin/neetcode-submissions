class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            nextCost = min(dfs(i+1), dfs(i+2))
            memo[i] = cost[i] + nextCost
            return memo[i]
        
        return min(dfs(0), dfs(1))
            