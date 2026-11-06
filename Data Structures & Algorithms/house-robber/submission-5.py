class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums) or i < 0:
                return 0
            if i in memo:
                return memo[i]
            robSpot = nums[i] + dfs(i+2)
            dontRob = dfs(i+1)
            memo[i] = max(robSpot, dontRob)
            return memo[i]
        return max(dfs(0), dfs(1))
            