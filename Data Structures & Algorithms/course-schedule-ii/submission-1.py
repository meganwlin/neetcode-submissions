class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inCount = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            inCount[course] += 1
            adjList[prereq].append(course)
        
        q = deque()
        answer = []
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            answer.append(course)
            for dependentCourse in adjList[course]:
                inCount[dependentCourse] -= 1
                if inCount[dependentCourse] == 0:
                    q.append(dependentCourse)
        
        if len(answer) != numCourses:
            return []
        return answer


        