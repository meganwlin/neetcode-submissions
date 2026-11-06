class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lower_index = 0
        upper_index = len(heights) - 1

        while lower_index < upper_index:
            height = min(heights[lower_index], heights[upper_index])
            width =  upper_index - lower_index
            area = height * width
            max_area = max(area, max_area)

            if  heights[lower_index] < heights[upper_index]:
                lower_index += 1
            else:
                upper_index -= 1
        return max_area

