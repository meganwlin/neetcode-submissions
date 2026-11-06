class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binaryMiddle(low, high):
            return (low + high) // 2

        def bananaHours(piles, k):
            hours = 0
            for p in piles:
                hours += (p // k)
                if ( p % k ) > 0:
                    hours += 1
            return hours
        
        low, high = 1, max(piles)
        k = high
        while low <= high:
            curr_k = binaryMiddle(low, high)

            hours = bananaHours(piles, curr_k)
            if hours <= h:
                k = min(k, curr_k)
                high = curr_k - 1
            elif hours > h:
                low = curr_k + 1
            else:
                pass
        return k
