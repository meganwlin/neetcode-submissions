class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        lower = 0
        upper = len(s) - 1

        while lower < upper:
            if not s[lower].isalnum():
                lower += 1
            elif not s[upper].isalnum():
                upper -= 1
            else:
                if s[lower] == s[upper]:
                    lower += 1
                    upper -= 1
                else:
                    return False
        return True