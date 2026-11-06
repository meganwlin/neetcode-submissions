class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for p in prices[1:]:
            if p < minBuy:
                minBuy = p
            else:
                profit = p - minBuy
                maxP = max(maxP, profit)
        return maxP



        
        