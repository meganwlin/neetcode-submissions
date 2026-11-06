class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            inDegree[b] += 1
            adjList[a].append(b)
        
        q = deque()
        for i, val in enumerate(inDegree):
            if val == 0:
                q.append(i)
        
        visited = set()
        while q:
            course = q.popleft()
            visited.add(course)
            for prereq in adjList[course]:
                inDegree[prereq] -= 1
                if inDegree[prereq] == 0:
                    q.append(prereq)
        
        if len(visited) == numCourses:
            return True
        return False
                
