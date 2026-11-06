class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l, r = 0, 1
        longest = 1
        nums = sorted(set(nums))
        print(nums)

        while r < len(nums):
            if nums[r] == nums[r-1] + 1:
                r += 1
            else:
                l = r
                r += 1
            longest = max(r - l, longest)
        return longest