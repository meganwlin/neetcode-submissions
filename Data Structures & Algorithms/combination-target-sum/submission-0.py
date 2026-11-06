class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(i, combo, total):
            if total == target:
                answer.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            total += nums[i]
            dfs(i, combo, total) # Choose the same number again
            combo.pop()
            total -=nums[i]
            dfs(i+1, combo, total) # Move on to add the next number in the list

        dfs(0, [], 0)

        return answer