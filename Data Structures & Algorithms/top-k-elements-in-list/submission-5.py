class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        maxHeap = []
        for num in d.keys():
            count = d[num]
            heapq.heappush(maxHeap, (-count, num))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(maxHeap)[1])
        return answer

