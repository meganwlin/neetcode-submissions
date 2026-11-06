class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            nextCost = min(dfs(i+1), dfs(i+2))
            memo[i] = cost[i] + nextCost
            return memo[i]
        
        return min(dfs(0), dfs(1))
            