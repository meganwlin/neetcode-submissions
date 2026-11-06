class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        
        for p in prices:
            if p < minBuy:
                minBuy = p
            else:
                maxProfit = max(maxProfit, p-minBuy)
        return maxProfit

