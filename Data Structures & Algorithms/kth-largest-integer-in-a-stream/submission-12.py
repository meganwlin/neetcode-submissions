class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        h = nums
        heapq.heapify(h)
        self.minheap = h
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
