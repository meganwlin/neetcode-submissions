class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        true_index = 0
        for i in nums:
            if i == val:
                continue
            else:
                nums[true_index] = i
                true_index += 1
        return true_index
        
