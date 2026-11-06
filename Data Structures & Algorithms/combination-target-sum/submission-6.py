class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(combo, i):
            nonlocal result
            # print(f"current combo is {combo} with sum: {sum(combo)}")
            if sum(combo) == target:
                result.append(combo.copy())
            elif sum(combo) > target:
                return
            elif i >= len(nums):
                return
            else:
                combo.append(nums[i])
                backtrack(combo, i)
                combo.pop()
                backtrack(combo, i+1)
                return
        
        backtrack([], 0)
        return result
