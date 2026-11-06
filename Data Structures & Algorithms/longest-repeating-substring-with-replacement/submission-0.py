class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dict = defaultdict(int)
        dict["!"] = 0
        maxLength = 0

        for r in range(len(s)):
            dict[s[r]] += 1
            while (r-l) - max(dict.values()) >= k and l <= r:
                dict[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r-l+1)
        return maxLength
                


