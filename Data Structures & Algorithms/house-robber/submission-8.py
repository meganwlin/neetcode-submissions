class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums): # OOB
                return 0
            elif memo[i] != -1:
                return memo[i]
            rob = nums[i] + dfs(i+2)
            dontRob = dfs(i+1)
            memo[i] = max(rob, dontRob)
            return memo[i]
        return dfs(0)
        