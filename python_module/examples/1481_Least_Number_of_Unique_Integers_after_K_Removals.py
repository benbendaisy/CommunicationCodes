class Solution:
    """
    Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

    Example 1:

    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.
    Example 2:
    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
    """
    def findLeastNumOfUniqueInts1(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        freq = list(freq_map.values())
        freq.sort()
        element_removed = 0
        for i in range(len(freq)):
            element_removed += freq[i]
            if element_removed > k:
                return len(freq) - i
        return 0
    
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        freq = list(freq_map.values())
        heapq.heapify(freq)
        element_removed = 0
        while freq:
            element_removed += heapq.heappop(freq)
            if element_removed > k:
                return len(freq) + 1
        return 0