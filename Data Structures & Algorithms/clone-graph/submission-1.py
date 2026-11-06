"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        mapping = {}
        mapping[node] = Node(node.val)

        def dfs(node):
            if not node:
                return
            for neighbor in node.neighbors:
                flag = False
                if neighbor not in mapping:
                    flag = True
                    # add new neighbor node to the map
                    mapping[neighbor] = Node(neighbor.val)

                # make edge
                neighbor_node = mapping[neighbor]
                mapping[node].neighbors.append(neighbor_node)

                if flag:
                    # recurse on nodes that don't exist yet
                    dfs(neighbor)
            return
        dfs(node)
        return mapping[node]

                
            
        