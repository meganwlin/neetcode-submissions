class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest_streak = 0
        for n in nums:
            curr_streak = 1
            while (n+curr_streak) in nums:
                curr_streak += 1
            longest_streak = max(longest_streak, curr_streak)
        return longest_streak
