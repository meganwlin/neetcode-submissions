class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(m) where m is unique letters
        letterMap = {}
        maxLen = 0
        start = 0

        for index, letter in enumerate(s):
            if letter in letterMap and letterMap[letter] >= start:
                # index of the previous time the duplicate letter was found
                start = letterMap[letter] + 1
            
            # add the letter to the map of found letters
            letterMap[letter] = index

            # calculate the maximum
            currLen = index - start + 1
            maxLen = max(maxLen, currLen)
        return maxLen
