from collections import Counter


class Solution:
    """
        Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

        Example 1:

        Input: s = "aaabb", k = 3
        Output: 3
        Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
        Example 2:

        Input: s = "ababbc", k = 2
        Output: 5
        Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

        Constraints:

        1 <= s.length <= 104
        s consists of only lowercase English letters.
        1 <= k <= 105
    """
    def longestSubstring1(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for i in range(1, 27):
            counter = Counter()
            j = 0
            for ch in s:
                if (ch in counter) or (len(counter) < i):
                    counter.update(ch)
                    val = 0
                    for key, value in counter.items():
                        if value < k:
                            val = 0
                            break
                        val += value
                    ans = max(ans, val)
                else:
                    while len(counter) == i:
                        counter[s[j]] -= 1
                        if counter[s[j]] == 0:
                            del counter[s[j]]
                        j += 1
                    counter.update(ch)
        return ans