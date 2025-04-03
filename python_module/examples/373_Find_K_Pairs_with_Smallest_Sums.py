import heapq
from typing import List


class Solution:
    """
        You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

        Define a pair (u, v) which consists of one element from the first array and one element from the second array.

        Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

        Example 1:

        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]
        Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
        Example 2:

        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [[1,1],[1,1]]
        Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
        Example 3:

        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [[1,3],[2,3]]
        Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

        Constraints:

        1 <= nums1.length, nums2.length <= 105
        -109 <= nums1[i], nums2[i] <= 109
        nums1 and nums2 both are sorted in ascending order.
        1 <= k <= 104
    """
    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited = set((0,0))
        res = []
        while minHeap and k > 0:
            _, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1 and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j < len(nums2) - 1 and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1
        return res
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 and not nums2:
            return []
        n1, n2 = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res, visited = [], set([(0, 0)])
        while len(res) < k:
            _, idx1, idx2 = heapq.heappop(heap)
            res.append((nums1[idx1], nums2[idx2]))
            if idx1 < n1 - 1:
                if (idx1 + 1, idx2) not in visited:
                    visited.add((idx1 + 1, idx2))
                    heapq.heappush(heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            
            if idx2 < n2 - 1:
                if (idx1, idx2 + 1) not in visited:
                    visited.add((idx1, idx2 + 1))
                    heapq.heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
        return res

