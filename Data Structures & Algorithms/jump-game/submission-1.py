class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        maxJump = nums[0]
        if maxJump:
            for i in range(1,maxJump+1):
                if self.canJump(nums[i:]):
                    return True
        return False
            