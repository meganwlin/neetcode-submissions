class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        leftMaxes = []
        rightMaxes = []

        for h in height:
            leftMax = max(leftMax, h)
            leftMaxes.append(leftMax)
        
        for h in height[::-1]:
            rightMax = max(rightMax, h)
            rightMaxes.append(rightMax)
        
        # reverse to set back to the correct order
        rightMaxes = rightMaxes[::-1]

        volume = 0
        for i in range(len(height)):
            h = height[i]
            l = leftMaxes[i]
            r = rightMaxes[i]
            if h < min(l, r):
                volume += min(l, r) - h
        return volume

        