class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            num = nums[m]
            if num == target:
                return m
            elif num < target:
                l = m + 1
            else:
                r = m - 1
        return -1