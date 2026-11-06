class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                # swap because cheaper price found
                l = r
                r += 1
                # print(f"{prices[r]} is less than {prices[l]} so swapping buy time to spot {l}")
            else:
                # print(f"New profit is {prices[r] - prices[l]}")
                answer = max(answer, prices[r] - prices[l])
                r += 1
        return answer
        