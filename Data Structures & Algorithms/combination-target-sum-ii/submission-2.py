class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(combo, i):
            nonlocal result
            # print(f"current combo is {combo} with sum: {sum(combo)}")
            if sum(combo) == target:
                result.append(combo.copy())
            elif sum(combo) > target:
                return
            elif i >= len(candidates):
                return
            else:
                combo.append(candidates[i])
                backtrack(combo, i+1)
                combo.pop()

                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i+=1

                backtrack(combo, i+1)
                return
        
        backtrack([], 0)
        return result