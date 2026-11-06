class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums = sorted(nums)

        c = []
        def combo(i):
            if i >= len(nums):
                return

            # select current
            c.append(nums[i])
            if sum(c) == target:
                answer.append(c.copy())
            elif sum(c) > target:
                c.pop()
                return

            # select current again
            combo(i)
            # select next
            c.pop()
            combo(i+1)
            
        combo(0)
        return answer
