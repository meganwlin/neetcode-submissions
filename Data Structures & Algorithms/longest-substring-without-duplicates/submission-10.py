class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        activeLetters = ""

        for letter in s:
            if letter in activeLetters:
                split = activeLetters.index(letter) + 1
                activeLetters = activeLetters[split:]

            activeLetters += letter
            # update length if this new substring is longer
            print(activeLetters)
            maxLen = max(maxLen, len(activeLetters))
        return maxLen