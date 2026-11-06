class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height is the min between two bars
        # width is diff between indices
        # area = height * width

        # running current maximum area we update as we move the pointers
        area = 0
        l, r = 0, len(heights) - 1 # start at opposite ends

        while l < r:
            currArea = (r-l) * min(heights[l], heights[r])
            # update the area based on current bars selected
            area = max(area, currArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area
            