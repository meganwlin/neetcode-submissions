class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inCount = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            inCount[a] += 1
            adjList[b].append(a)
        
        q = deque()
        visited = set()

        for i, val in enumerate(inCount):
            if val == 0:
                q.append(i)
        
        while q:
            prereq = q.popleft()
            print(prereq)
            for course in adjList[prereq]:
                inCount[course] -= 1
                if inCount[course] == 0:
                    print(f"Adding course {course}")
                    q.append(course)
            visited.add(prereq)
        return len(visited) == numCourses