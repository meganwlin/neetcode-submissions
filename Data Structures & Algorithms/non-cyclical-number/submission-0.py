class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate(a: int) -> int:
            total = 0
            for digit in str(a):
                total += int(digit) ** 2
            return total
        
        while n!= 1:
            new = calculate(n)
            if new in seen:
                return False
            seen.add(new)
            n = new
        return True
