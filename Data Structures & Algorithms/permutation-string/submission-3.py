class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s1) == 0:
            return True

        d1 = [0] * 26
        d2 = [0] * 26

        for letter in s1:
            index = ord(letter) - ord('a')
            d1[index] += 1
        
        # Make an initial frequency map
        for letter in s2[:len(s1)]:
            index = ord(letter) - ord('a')
            d2[index] += 1

        if d1 == d2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            new_letter = s2[r]
            old_letter = s2[l]

            d2[ord(new_letter) - ord('a')] += 1
            d2[ord(old_letter) - ord('a')] -=1

            if d1 == d2:
                return True
            l+=1
        return False


        
