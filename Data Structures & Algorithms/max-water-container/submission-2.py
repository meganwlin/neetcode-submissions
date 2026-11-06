class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            total = height * width
            answer = max(answer, total)

            # left is the shorter wall
            if height == heights[l]:
                l += 1
            else:
                r -= 1

        return answer