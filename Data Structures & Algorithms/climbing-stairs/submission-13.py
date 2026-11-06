class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = 1
        for i in range(n+1):
            one = i+1
            two = i+2

            if one <= n:
                cache[one] += cache[i]
            if two <= n:
                cache[two] += cache[i]
        return cache[n]