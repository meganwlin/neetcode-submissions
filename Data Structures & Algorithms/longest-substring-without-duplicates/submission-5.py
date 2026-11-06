class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = ""
        maxLength = 0

        for letter in s:
            found_index = used.find(letter)
            if found_index > -1:
                maxLength = max(maxLength, len(used))
                used = used[found_index + 1:]
            used += letter
        return max(maxLength, len(used))

