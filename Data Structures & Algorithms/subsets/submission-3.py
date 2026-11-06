class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        s = []
        def subset(i):
            if i >= len(nums):
                return
            s.append(nums[i])
            subset(i+1)
            answer.append(s.copy())
            s.pop()
            subset(i+1)
            return
        subset(0)
        return answer