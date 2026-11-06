class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowK = 1
        highK = max(piles)

        while lowK < highK:
            k = (lowK + highK)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            
            if totalTime > h:
                lowK = k + 1
            else:
                highK = k
        return lowK