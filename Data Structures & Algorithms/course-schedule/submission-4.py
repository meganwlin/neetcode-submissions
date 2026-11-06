class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inCount = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            inCount[course] += 1
            adjList[prereq].append(course)
        
        q = deque()
        
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
        
        courseTaken = len(q)
        while q:
            prereq = q.popleft()
            for course in adjList[prereq]:
                inCount[course] -= 1
                if inCount[course] == 0:
                    q.append(course)
                    courseTaken += 1
        return courseTaken == numCourses

