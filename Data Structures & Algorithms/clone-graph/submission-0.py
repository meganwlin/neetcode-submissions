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
            return None

        mapping = {}

        # set up first node
        mapping[node] = Node(node.val)

        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()
            print(f"Evaluating node {curr_node.val}")

            # add neighbors to the queue
            for neighbor in curr_node.neighbors:
                if neighbor not in mapping:
                    print(f"Neighbor {neighbor.val} doesn't exist yet")
                    # unvisited node, continue cloning
                    queue.append(neighbor) # add the original neighbor node to traverse
                    mapping[neighbor] = Node(neighbor.val) # create cloned node without neighbors
                # always create an edge
                mapping[curr_node].neighbors.append(mapping[neighbor])
        
        return mapping[node]