class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)
        def dfs(i):
            if i < 0:
                return 0
            if mem[i] > -1:
                return mem[i]
            money = nums[i] + max(dfs(i-2), dfs(i-3))
            mem[i] = money
            return money
        return max(dfs(len(nums)-1), dfs(len(nums)-2))
