class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def dfs(i):
            if i == len(nums):
                answer.append(subset.copy())
                return
            # select
            subset.append(nums[i])
            # recurse
            dfs(i+1)
            # deselect
            subset.pop()
            # recurse
            dfs(i+1)
            return
        dfs(0)
        return answer
