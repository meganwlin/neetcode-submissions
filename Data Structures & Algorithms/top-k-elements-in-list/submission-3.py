class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency count of each number
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        # top k elements
        heap = []
        for key, v in freq.items():
            heapq.heappush(heap, (-v, key))
        
        answer = []
        for i in range(0, k):
            topK = heapq.heappop(heap)
            answer.append(topK[1])
        return answer
