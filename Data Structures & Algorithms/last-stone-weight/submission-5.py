class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            print(f"Stones: {stones}")
            # get heaviest stone
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            smashed = abs(x - y)
            heapq.heappush(stones, -smashed)
        return -stones[-1]