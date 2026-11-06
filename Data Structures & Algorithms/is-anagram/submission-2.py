class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        a = defaultdict(int)
        b = defaultdict(int)

        for letter in s:
            a[letter] += 1
        for letter in t:
            b[letter] += 1
        
        return a == b
            
