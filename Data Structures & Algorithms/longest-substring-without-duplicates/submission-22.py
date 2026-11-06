class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqMap = {}
        left = 0
        longest = 0


        for i, char in enumerate(s):
            if char in freqMap:
                left = max(left, freqMap[char] + 1)
            length = i - left + 1
            longest = max(longest, length)
            freqMap[char] = i
        return longest
