class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keeps track of freq of each char
        d = defaultdict(int)
        longestStr = 0

        l, r = 0, 0
        while l < len(s) and r < len(s):
            char = s[r]
            if d[char] == 0:
                d[char] += 1
                r += 1
                longestStr = max(r-l, longestStr)
            else:
                # keep moving left pointer until we eliminate the duplicate character
                prefix = s[l]
                d[prefix] -= 1
                l += 1
                # don't increment r, will enter this same elimination trigger if not all duplicates found
        return longestStr




        