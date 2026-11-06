class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        total = 0
        for r, char in enumerate(s):
            if char in map:
                # move pointer to exclude former instance 
                l = max(map[char] + 1, l)
            map[char] = r
            total = max(total, r - l + 1)
        return total

            
