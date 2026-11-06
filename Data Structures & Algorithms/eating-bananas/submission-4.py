class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def calculateHours(k):
            time = 0
            for p in piles:
                time += p // k
                if p % k > 0:
                    time += 1
            return time
        
        while l < r:
            k = (l + r) // 2

            hours = calculateHours(k)

            if hours > h:
                l = k + 1
            else:
                r = k
        return l

                