class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        total = 0
        lMax, rMax = height[l], height[r]
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(height[l], lMax)
                total += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r], rMax)
                total += rMax - height[r]
        return total



