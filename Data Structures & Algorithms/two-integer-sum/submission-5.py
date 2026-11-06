class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in d:
                return [d[complement], i]
            else:
                d[n] = i
        return [-1,-1]
        