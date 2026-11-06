class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights[i+1:]):
                height = min(h1, h2)
                area = height * (j+1)
                max_area = max(area, max_area)
        return max_area

