class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1

        while min <= max:
            index = min + (max - min)//2

            if nums[index] > target:
                max = index - 1
            elif nums[index] < target:
                min = index + 1
            else:
                return index
        return -1

        