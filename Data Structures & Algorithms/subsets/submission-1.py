class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [] # final list of answers
        subset = [] # current individual subset

        def dfs(i):
            if i >= len(nums):
                answer.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return answer
        