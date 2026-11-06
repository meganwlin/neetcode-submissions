class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1
        
        for char in t:
            counter[char] -= 1
            if counter[char] < 0:
                print(char, counter)
                return False
        return True
