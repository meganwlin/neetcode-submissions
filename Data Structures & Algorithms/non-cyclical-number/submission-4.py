class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow!=fast:
            # increase fast by 2
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)

            slow = self.sumOfSquares(slow)

        return fast == 1

    def sumOfSquares(self, n: int) -> int:
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            return total    
