from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_cnt_dict = Counter(nums1)
        arr = []
        for num in nums2:
            if num in nums_cnt_dict and nums_cnt_dict[num] > 0:
                arr.append(num)
                nums_cnt_dict[num] -= 1
        return arr

