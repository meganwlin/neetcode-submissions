class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        for i, t1 in enumerate(temperatures):
            for diff, t2 in enumerate(temperatures[i+1:]):
                if t2 > t1:
                    answer[i] = diff + 1
                    break
        return answer
            

        