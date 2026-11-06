class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            smashed = x - y

            if smashed != 0:
                heapq.heappush(stones, -smashed)
        if len(stones) == 0:
            return 0
        else:
            return -heapq.heappop(stones)

        