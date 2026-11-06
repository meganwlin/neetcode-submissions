class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i, n in enumerate(nums):
            if nums[i+1] == n:
                return n
        return -1