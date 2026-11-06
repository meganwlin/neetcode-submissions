class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]
        inCount = [0] * numCourses

        for a, b in prerequisites:
            adjList[a].append(b)
            inCount[b] += 1
        
        visited = set()
        q = deque()
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
                visited.add(i)
        
        while q:
            course = q.popleft()
            for prereq in adjList[course]:
                inCount[prereq] -= 1
                if inCount[prereq] == 0:
                    q.append(prereq)
                    visited.add(prereq)
        
        if len(visited) == numCourses:
            return True
        return False
