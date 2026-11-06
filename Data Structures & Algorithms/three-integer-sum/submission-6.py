class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []

        for i in range(0, len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in answer:
                            answer.append(triplet)
                    if total > 0:
                        break
        return answer
