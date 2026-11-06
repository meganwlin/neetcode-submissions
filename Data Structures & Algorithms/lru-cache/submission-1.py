class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            val = node.val
            self.removeNode(node)
            self.addNode(key, val)
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        elif len(self.cache) >= self.capacity:
            self.removeNode(self.head)
        self.addNode(key, value)
    
    # adds to the end of the cache
    def addNode(self, key, value):
        add = Node(key, value)
        if not self.tail:
            self.head = add
            self.tail = add
        else:
            self.tail.next = add
            add.prev = self.tail
            self.tail = add
        self.cache[key] = add
        return add
    
    def removeNode(self, node):
        next_node, prev_node = node.next, node.prev
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        if node.key in self.cache:
            del self.cache[node.key]
