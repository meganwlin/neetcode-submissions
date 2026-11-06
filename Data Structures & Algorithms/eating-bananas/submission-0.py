class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        speed = maxK
        while minK <= maxK:
            # Use the midpoint, binary search
            k = (maxK + minK) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            
            if hours <= h:
                maxK = k-1
                speed = k
            else:
                minK = k+1
        return speed


        