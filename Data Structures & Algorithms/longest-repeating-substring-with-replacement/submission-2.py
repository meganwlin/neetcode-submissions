class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        longest = 0
        l = 0
        maxF = 0

        # iterate through each letter
        for r, char in enumerate(s):
            char_count = freq.get(char, 0) + 1
            # add char to current substring
            freq[char] = char_count
            maxF = max(maxF, char_count)

            # if over k replacements needed, start popping
            while(r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest


            




        