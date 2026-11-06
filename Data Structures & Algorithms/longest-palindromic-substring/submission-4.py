class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkEven(i):
            length = 0
            subs = ""
            j = i + 1
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    subs = s[i] + subs + s[j]
                    length += 2
                    i -= 1
                    j += 1
                else:
                    break
            return length, subs

        def checkOdd(i):
            length = 1
            subs = s[i]
            l, r = i-1, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    subs = s[l] + subs + s[r]
                    length += 2
                    l -= 1
                    r += 1
                else:
                    break
            return length, subs
        
        longest = 0
        longestStr = ""
        for i in range(len(s)):
            evenLen, evenStr = checkEven(i)
            oddLen, oddStr = checkOdd(i)
            
            if evenLen > longest:
                longestStr = evenStr
                longest = evenLen
            if oddLen > longest:
                longestStr = oddStr
                longest = oddLen
        return longestStr

        