class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        upper = len(numbers) - 1
        total = numbers[lower] + numbers[upper]

        while lower < upper:
            total = numbers[lower] + numbers[upper]
            if total == target:
                return [lower + 1, upper + 1]
            elif total < target:
                lower += 1
            elif total > target: 
                upper -= 1
        return [lower, upper]