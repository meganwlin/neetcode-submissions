class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        alphanum = "0123456789abcdefghijklmnopqrstuvwxyz"
        while l <= r:
            while s[l] not in alphanum:
                l += 1
                if l >= len(s):
                    return True
            while s[r] not in alphanum:
                r -= 1
                if r < 0:
                    return True
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
