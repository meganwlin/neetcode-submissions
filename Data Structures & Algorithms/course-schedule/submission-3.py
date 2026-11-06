class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inCount = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            inCount[prereq] += 1
            adjList[course].append(prereq)
        
        q = deque()
        
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
        
        courseTaken = len(q)
        while q:
            course = q.popleft()
            for prereq in adjList[course]:
                inCount[prereq] -= 1
                if inCount[prereq] == 0:
                    q.append(prereq)
                    courseTaken += 1
        return courseTaken == numCourses

