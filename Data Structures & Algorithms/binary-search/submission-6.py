class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1

        while l <= u:
            m = ((u - l) // 2) + l
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                u = m - 1
        return -1
