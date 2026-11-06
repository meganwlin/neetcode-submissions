class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = 0

        for p in prices:
            if p > minP:
                maxP = max(maxP, p - minP)
            else:
                minP = min(minP, p)
        return maxP
        