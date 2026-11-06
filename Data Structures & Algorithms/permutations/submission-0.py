class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(combo: List[int], remaining: List[int]):
            if len(remaining) == 0:
                answer.append(combo.copy())
            for i in range(len(remaining)):
                combo.append(remaining[i])
                dfs(combo, remaining[:i] + remaining[i+1:])
                combo.pop()
        dfs([], nums)
        return answer
