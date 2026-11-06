class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            # When nums[m] is less than nums[r], the minimum must be in the left half
            if nums[m] < nums[r]:
                r = m
            # When nums[m] is greater than or equal to nums[r], the minimum is in the right half
            else:
                l = m + 1
        # The loop will end when l == r, pointing to the smallest element
        return nums[l]
