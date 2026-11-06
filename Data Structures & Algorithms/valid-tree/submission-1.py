class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visit = set()

        def dfs(node, parent):
            # we have already visited this node before which means it is a cycle
            if node in visit:
                return False
            
            # new node, mark it as such so we don't visit it again
            visit.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue # we just backtracked which is fine
                if not dfs(nei ,node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n