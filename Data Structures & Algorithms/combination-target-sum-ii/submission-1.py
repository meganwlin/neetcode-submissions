class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates = sorted(candidates)

        combo = []
        def dfs(i, total):
            if total == target:
                answer.append(combo.copy())
            elif total > target or i >= len(candidates):
                return
            else:
                # select
                num = candidates[i]
                combo.append(num)
                dfs(i+1, total + num)

                # unselect
                combo.pop()
                i += 1
                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i += 1
                dfs(i, total)
        dfs(0,0)
        return answer