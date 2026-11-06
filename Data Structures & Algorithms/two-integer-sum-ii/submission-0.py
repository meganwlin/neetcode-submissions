class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            complement = target - n
            if complement in d:
                return [d[complement], i + 1]
            else:
                d[n] = i + 1
        return [0,0]
