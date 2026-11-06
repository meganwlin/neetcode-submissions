class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        # key is the map of the counts by letter
        # value is the strings

        for s in strs:
            letterMap = [0] * 26
            for letter in s:
                # index is the num letters in the alphabet from a
                letterMap[ord(letter) - ord('a')] += 1
            # a list cannot be a key, but a tuple can bc it is immutable
            anagramMap[tuple(letterMap)].append(s)
        return anagramMap.values()
