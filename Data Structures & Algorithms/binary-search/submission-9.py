class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            n = nums[mid]
            if n == target:
                return mid
            elif n < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        