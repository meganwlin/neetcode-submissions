class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i: int, path: List[int], target: int):
            currentSum = sum(path)
            if currentSum == target:
                if path not in res:
                    res.append(path)
                return
            if currentSum > target:
                return
            
            for i2 in range(i+1, len(candidates)):
                #  add to path (select)
                dfs(i2, path + [candidates[i2]], target)
                # skip adding
        
        dfs(-1, [], target) # index, path, target
        return res
