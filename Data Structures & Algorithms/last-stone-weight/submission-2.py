class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest_stone = heapq.heappop(stones)
            next_stone = heapq.heappop(stones)
            diff = heaviest_stone - next_stone
            if diff:
                heapq.heappush(stones, diff)
        if stones:
            return -stones[0]
        else:
            return 0
