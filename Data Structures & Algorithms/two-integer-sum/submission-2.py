class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = 0
        for n in nums:
            complement = target - n
            if complement in dict:
                return [dict[complement], index]
            dict[n] = index
            index += 1

        