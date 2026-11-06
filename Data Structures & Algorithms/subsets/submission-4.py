class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def dfs(n):
            if n >= len(nums):
                answer.append(subset.copy())
                return
            subset.append(nums[n])
            dfs(n+1)
            subset.pop()
            dfs(n+1)
        dfs(0)
        return answer