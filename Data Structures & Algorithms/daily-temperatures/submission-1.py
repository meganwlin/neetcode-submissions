class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
        [1, 5, 2, 10, 7]
        '''
        answer = [0] * len(temperatures)
        stack = [] # index, temp

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                update_idx, t2 = stack.pop()
                answer[update_idx] = i - update_idx
            stack.append((i, t))
        return answer




        
            

        