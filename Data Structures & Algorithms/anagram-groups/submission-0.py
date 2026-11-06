class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            a = ''.join(sorted(s))
            anagrams[a].append(s)
        
        return list(anagrams.values())