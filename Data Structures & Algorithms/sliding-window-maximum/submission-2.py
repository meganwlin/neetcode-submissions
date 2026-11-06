class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        l, r = 0, k-1
        arr = []

        # Find the initial max of the first window
        high, maxIndex = self.calculateMaxAndIndex(nums[:k], 0)
        arr.append(high)

        # Slide the window over the rest of the array
        while r < len(nums) - 1:
            l += 1
            r += 1
            # Update the max if the new element is larger
            if nums[r] >= high:
                maxIndex = r
                high = nums[r]
            else:
                # If the new window doesn't contain the previous max, recalculate
                if r >= maxIndex:
                    high, maxIndex = self.calculateMaxAndIndex(nums[l:r+1], l)

            # Append the current max of the window
            arr.append(high)

        return arr

    def calculateMaxAndIndex(self, nums: List[int], l: int):
        high = max(nums)
        index = nums.index(high)
        return high, index + l
