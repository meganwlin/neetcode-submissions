class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        minHeap = []

        for key, value in d.items():
            heapq.heappush(minHeap, [-value, key])
        
        answer = []
        while len(answer) < k:
            count, num = heapq.heappop(minHeap)
            answer.append(num)
        return answer
