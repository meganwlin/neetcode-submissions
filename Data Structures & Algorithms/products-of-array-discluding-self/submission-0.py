class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all = 1
        zero_count = 0
        for n in nums:
            if n != 0:
                all *= n
            else:
                zero_count += 1
        
        answer = []
        if zero_count > 1:
            for n in nums:
                answer.append(0)
        elif zero_count > 0:
            for n in nums:
                if n == 0:
                    answer.append(all)
                else:
                    answer.append(0)
        else:
            for n in nums:
                answer.append(int(all/n))
        return answer