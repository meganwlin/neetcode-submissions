class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = [-s for s in stones]
        heapq.heapify(rocks)

        while len(rocks) > 1:
            x = heapq.heappop(rocks)
            y = heapq.heappop(rocks)

            smash = y - x
            if smash:
                heapq.heappush(rocks, -smash)
        if len(rocks) == 1:
            return -rocks[0]
        else:
            return 0
