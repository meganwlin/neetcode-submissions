class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hoursNeeded(k):
            hours = 0
            for p in piles:
                hours += p // k
                if p % k != 0:
                    hours += 1
            return hours
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) //2
            hours = hoursNeeded(mid)

            if hours > h:
                l = mid + 1
            else:
                r = mid
        return l