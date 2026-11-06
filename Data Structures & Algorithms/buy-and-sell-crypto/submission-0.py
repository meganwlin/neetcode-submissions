class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0,1
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            profit = sell-buy
            maxProfit = max(maxProfit, profit)

            if sell < buy:
                l = r
            else:
                r += 1
        return maxProfit

