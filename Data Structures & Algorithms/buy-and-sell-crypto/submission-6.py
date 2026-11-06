class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            buy, sell = prices[l], prices[r]
            profit = sell - buy
            maxProfit = max(maxProfit, profit)

            if buy > sell:
                l = r
            r += 1
        return maxProfit