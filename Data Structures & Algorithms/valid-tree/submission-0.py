class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        q = deque()
        q.append([0, -1])
        visited = set()
        visited.add(0)

        while q:
            node, parent = q.popleft()

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append([nei, node])
                visited.add(nei)
        return len(visited) == n
        