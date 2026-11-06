class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        buckets = [[] for n in range(len(nums)+1)]
        for n in nums:
            counter[n] += 1
            buckets[counter[n]].append(n)
        
        answer = set()
        for bucket in buckets[::-1]:
            answer.update(bucket)
            if len(answer) >= k:
                break
        return list(answer)
            

