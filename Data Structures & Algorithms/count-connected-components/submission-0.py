class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        answer = 0
        visited = set()

        for i in range(n):
            # already looked at this node so skip it
            if i in visited:
                continue
            
            q = deque()
            q.append(i)
            while q:
                curr = q.popleft()
                for j in adj[curr]:
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
            answer += 1
        return answer



        