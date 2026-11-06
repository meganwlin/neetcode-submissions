class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        subset = []
        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                return
            if sum(subset) == target:
                answer.append(subset.copy())
                return
            elif sum(subset) > target:
                return
            
            # choose the same number again
            subset.append(nums[i])
            dfs(i)
            # deselect
            subset.pop()
            dfs(i+1)

        dfs(0)
        return answer
            