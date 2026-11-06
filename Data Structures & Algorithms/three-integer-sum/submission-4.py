class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            a_val = nums[i]
            if a_val == nums[i-1] and i > 0:
                print("continue")
                continue
            if a_val > 0:
                break
            for j in range(i + 1, len(nums)):
                b_val = nums[j]
                if b_val == nums[j-1] and j > i + 1:
                    continue
                target = -(a_val + b_val)

                # j has become too large as k must be positive to balance
                if target < 0:
                    break
                
                if nums[j+1:].count(target) > 0:
                    new_triple = [[a_val, b_val, target]]
                    answer.append([a_val, b_val, target])
        return answer

