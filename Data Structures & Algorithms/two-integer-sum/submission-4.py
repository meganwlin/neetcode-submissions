class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} # value, index
        for i, n in enumerate(nums):
            m = target - n
            if m in mp:
                return [mp[m], i]
            else:
                mp[n] = i
        return [0,0]
        