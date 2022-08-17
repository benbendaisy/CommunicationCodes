from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Dict = Counter(nums2)
        arr = []
        for v in nums1:
            if v in nums2Dict and nums2Dict[v] > 0:
                arr.append(v)
                nums2Dict[v] -= 1
        return arr

