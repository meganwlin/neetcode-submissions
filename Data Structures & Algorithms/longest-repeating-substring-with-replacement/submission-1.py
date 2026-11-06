class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        res = 0
        mp = {}
        l = 0

        for r, char in enumerate(s):
            # get count up to this point
            mp[char] = mp.get(char, 0) + 1

            maxF = max(maxF, mp[char])

            while ((r - l + 1) - maxF) > k:
                remove_char = s[l]
                mp[remove_char] -= 1
                l += 1
            res = max(res, r-l +1)
        return res
