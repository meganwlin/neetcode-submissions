class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            max_j = min(len(nums) - 1, i + k + 1)
            print(i, max_j)
            print(range (i+1, max_j))
            for j in range(i+1, min(len(nums), i + k + 1)):
                if nums[i] == nums[j]:
                    return True
        
        return False