class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        def combos(nums: List[int], combo: List[int]) -> List[List[int]]:
            if not nums:
                return
            for i, n in enumerate(nums):
                combo.append(n)
                answer.append(combo.copy())
                combos(nums[i+1:], combo)

                # Deselect
                combo.pop()
            return
        combos(nums, [])
        return answer


        