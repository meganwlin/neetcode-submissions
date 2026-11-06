class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 1
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            d += carryover
            
            carryover = d // 10
            digits[i] = d % 10
            
        if carryover:
            return [carryover] + digits
        else:
            return digits