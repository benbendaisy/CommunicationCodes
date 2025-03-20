from collections import Counter, defaultdict
from typing import List


class Solution:
    """
        Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

        Example 1:

        Input: arr = [1,2,2,1,1,3]
        Output: true
        Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
        Example 2:

        Input: arr = [1,2]
        Output: false
        Example 3:

        Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
        Output: true
    """
    def uniqueOccurrences1(self, arr: List[int]) -> bool:
        count_map = Counter(arr)
        cnt_list = defaultdict(list)
        for k, v in count_map.items():
            cnt_list[v].append(k)
        for k, v in cnt_list.items():
            if len(v) > 1:
                return False
        return True

    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        count_map = Counter(arr)
        cnt_list = defaultdict(list)
        for k, v in count_map.items():
            if len(cnt_list[v]) > 0:
                return False
            cnt_list[v].append(k)
        return True
    
    def uniqueOccurrences3(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        freq_set = set(freq.values())
        return len(freq) == len(freq_set)
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        values = set(freq.values())
        return len(freq) == len(values)