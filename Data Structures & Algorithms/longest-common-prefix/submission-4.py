class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = 0
        while longest < len(strs[0]):
            letter = strs[0][longest]
            for s in strs:
                if len(s)== 0:
                    return ""
                if longest >= len(s):
                    return strs[0][:longest]
                if s[longest] != letter:
                    return strs[0][:longest]
            longest += 1
        return strs[0][:longest]
