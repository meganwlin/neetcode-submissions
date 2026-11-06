class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down
        cache = [-1] * (len(cost) + 1)

        def dfs(n):
            if n == 0 or n == 1:
                return cost[n]
            if cache[n] != -1:
                return cache[n]
            cache[n] = min(dfs(n-1), dfs(n-2)) + cost[n]
            return cache[n]
        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))