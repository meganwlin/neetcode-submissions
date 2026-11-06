class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = [] # final list of combos

        def dfs(i, combo):
            if sum(combo) == target:
                answer.append(combo.copy())
            else:
                for j in range(i, len(nums)):
                    if sum(combo) + nums[j] > target:
                        return
                    combo.append(nums[j])
                    dfs(j, combo)
                    combo.pop()
        dfs(0, [])
        return answer
            
