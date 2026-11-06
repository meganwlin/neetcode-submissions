class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        combo = []

        def dfs(i):
            if i == len(nums):
                return
            if sum(combo) == target:
                answer.append(combo.copy())
                return
            elif sum(combo) > target:
                return
            else:
                # select
                combo.append(nums[i])
                dfs(i)
                # deselect
                combo.pop()
                dfs(i + 1)
                return
        dfs(0)
        return answer