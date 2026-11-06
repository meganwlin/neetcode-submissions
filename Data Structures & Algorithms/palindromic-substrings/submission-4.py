class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if (j - i) <=2 and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1] == True:
                        dp[i][j] = True
                        res += 1
        return res

        