class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            d[key].append(s)
        # print(d)
        
        answer = []
        for anagram in d.values():
            answer.append(anagram)
        return answer