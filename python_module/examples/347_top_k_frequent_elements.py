import heapq
from collections import defaultdict, Counter
from typing import List


class Solution:
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) <= k:
            return nums

        freqMap = Counter(nums)

        return heapq.nlargest(k, freqMap.keys(), key=freqMap.get)

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) <= k:
            return nums
        freq_map = Counter(nums)
        return [k for k, v in sorted(freq_map.items(), key=lambda x: x[1], reverse=True)][:k]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freqMap = defaultdict(int)
        for it in nums:
            freqMap[it] += 1

        return [k for k, v in sorted(freqMap.items(), key=lambda it: it[1], reverse=True)][:k]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        num_dict = Counter(nums)
        return [num[0] for num in num_dict.most_common()[:k]]

