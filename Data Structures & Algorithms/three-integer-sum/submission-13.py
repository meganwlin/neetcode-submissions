class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(n log(n))
        answer = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                # skip this so we don't have duplicates
            elif nums[i] > 0:
                break
                # only positives from here so break early
            else:
                l, r = i+1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]

                    if total < 0:
                        l += 1
                    elif total > 0:
                        r -= 1
                    else: # total == 0
                        answer.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return answer



