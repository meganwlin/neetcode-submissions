class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inCount = [0] * numCourses
        adj = [[] for n in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)
            inCount[a] += 1
        
        q = deque()
        visited = set()
        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i) # add all the courses with no prerequisites and take them first
        
        while q:
            course = q.popleft()
            visited.add(course)
            for dependent in adj[course]:
                inCount[dependent] -= 1
                if inCount[dependent] == 0:
                    # no more prerequisites, can take this course
                    q.append(dependent)
        return len(visited) == numCourses

