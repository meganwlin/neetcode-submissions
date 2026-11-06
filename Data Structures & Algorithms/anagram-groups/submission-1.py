class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            identifier = ''.join(sorted(s))
            d[identifier].append(s)
        return d.values()
