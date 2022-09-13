import heapq
from collections import Counter


class Solution:
    """
        Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".

        Example 1:

        Input: s = "aabbcc", k = 3
        Output: "abcabc"
        Explanation: The same letters are at least a distance of 3 from each other.
        Example 2:

        Input: s = "aaabc", k = 3
        Output: ""
        Explanation: It is not possible to rearrange the string.
        Example 3:

        Input: s = "aaadbbcc", k = 2
        Output: "abacabcd"
        Explanation: The same letters are at least a distance of 2 from each other.

        Constraints:

        1 <= s.length <= 3 * 105
        s consists of only lowercase English letters.
        0 <= k <= s.length
    """
    def rearrangeString(self, s: str, k: int) -> str:
        charDict = Counter(s)
        # max heap
        heap = []
        for k, v in charDict.items():
            heapq.heappush(heap, (-v, k))

        heapK = []
        res = ""
        while heap:
            top = heapq.heappop(heap)
            res += top[1]
            # -top[0] is the num of keys left
            if -top[0] - 1 > 0: # if there is key left
                heapq.heappush(heapK, (len(res) - 1, -top[0] - 1, top[1]))

            if heapK and heapK[0][0] + k <= len(res):
                topK = heapq.heappop(heapK)
                heapq.heappush(heap, (-topK[1], topK[2]))
        return res if len(s) == len(res) else ""