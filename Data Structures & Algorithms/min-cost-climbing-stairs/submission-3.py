class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        totalCost = 0
        while n > 1:
            one_step = cost[n-1]
            two_step = cost[n-2]

            if one_step < two_step:
                n -= 1
            else:
                n -= 2
            
            totalCost += min(one_step, two_step)
        return totalCost


