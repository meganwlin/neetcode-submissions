class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        num_dict = defaultdict(int)
        for n in nums:
            num_dict[n] += 1

        nums = sorted(nums)
        for i in range(len(nums) - 2):
            # if smallest value is slready positive, no more to find
            if nums[i] > 0:
                break

            # skip duplicates
            if i != 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums) - 1):
                # skip duplicates
                if j != (i+1) and nums[j] == nums[j-1]:
                    continue

                total = nums[i] + nums[j]
                complement = -total

                # third number must be larger than already used
                if complement < nums[j]:
                    continue

                threshold = 0
                if complement == nums[i]:
                    threshold += 1
                if complement == nums[j]:
                    threshold += 1
                if num_dict[complement] > threshold:
                    answer.append([nums[i], nums[j], complement])
        return answer

                
                
                
            
