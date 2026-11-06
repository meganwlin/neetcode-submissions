class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        w = 0
        while l < r:
            curr_w = min(heights[l], heights[r]) * (r - l)
            w = max(curr_w, w)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return w
