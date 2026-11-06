class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # store the cost to get to that step so far
        memo = [-1] * len(cost)

        def climbStair(n): # step you are on
            if n >= len(cost):
                return 0
            if memo[n] != -1:
                return memo[n]
            else:
                memo[n] = cost[n] + min(climbStair(n+1), climbStair(n+2))
                return memo[n]

        return min(climbStair(0), climbStair(1))
