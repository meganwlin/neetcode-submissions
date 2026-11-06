class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return ((x**2 + y**2)**0.5)
        
        minHeap = []
        for point in points:
            d = distance(point[0], point[1])
            minHeap.append([d, point])
        heapq.heapify(minHeap)
        answer = []
        while len(answer) < k:
            dist, point = heapq.heappop(minHeap)
            answer.append(point)
        return answer