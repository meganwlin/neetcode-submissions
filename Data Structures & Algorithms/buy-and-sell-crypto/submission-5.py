class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]
        
        for p in prices:
            lowest = min(p, lowest)
            maxP = max(maxP, p - lowest)
        return maxP



