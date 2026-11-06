class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(list)
        for n in set(nums):
            counts[nums.count(n)].append(n)
        answer = []
        sorted_counts = sorted(counts.keys())

        while len(answer) < k:
            answer+=(counts[sorted_counts.pop()])

        return answer
        