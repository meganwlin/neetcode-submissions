class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for i in range (1, len(nums)):
            temp_addition = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp_addition = max(temp_addition, lis[j])
            lis[i] += temp_addition
        return max(lis)