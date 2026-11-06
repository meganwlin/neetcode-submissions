class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        inCount = [0] * numCourses

        for a, b in prerequisites:
            adjList[a].append(b)
            inCount[b] += 1

        answer = []

        q = deque()
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            answer.append(c)

            for prereq in adjList[c]:
                inCount[prereq] -=1
                if inCount[prereq] == 0:
                    q.append(prereq)
            
        if len(answer) != numCourses:
            return []
        else:
            return answer[::-1]

        