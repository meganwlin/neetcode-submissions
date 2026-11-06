class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower,  upper = 0, len(nums) - 1

        while lower <= upper:
            m = lower + (upper - lower) // 2
            if target == nums[m]:
                return m

            if nums[lower] <= nums[m]: # lower half is sorted
                if target < nums[lower] or target > nums[m]: #only look at the upper half
                    lower = m + 1
                else:
                    upper = m - 1
            else:
                if target > nums[upper] or target < nums[m]:
                    upper = m - 1
                else:
                    lower = m + 1
        return -1