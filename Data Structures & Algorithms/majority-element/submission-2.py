class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = set(nums)

        for n in unique:
            if nums.count(n) > (len(nums)/2):
                return n
        return nums[0]