class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for p in points:
            x, y = p[0], p[1]
            distance = x ** 2 + y ** 2
            min_heap.append((distance, [x, y]))
        
        heapq.heapify(min_heap)
        answer = []
        while len(answer) < k:
            next = heapq.heappop(min_heap)
            answer.append(next[1])
        return answer