class Solution:
    """
        Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

        Example 1:

        Input: s = "00110110", k = 2
        Output: true
        Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
        Example 2:

        Input: s = "0110", k = 1
        Output: true
        Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
        Example 3:

        Input: s = "0110", k = 2
        Output: false
        Explanation: The binary code "00" is of length 2 and does not exist in the array.

        Constraints:

        1 <= s.length <= 5 * 105
        s[i] is either '0' or '1'.
        1 <= k <= 20
    """
    def hasAllCodes1(self, s: str, k: int) -> bool:
        cnt = 1 << k
        seen = set()
        for i in range(k, len(s) + 1):
            temp = s[i - k:i]
            if temp not in seen:
                seen.add(temp)
                cnt -= 1
                if cnt == 0:
                    return True
        return False

    def hasAllCodes2(self, s: str, k: int) -> bool:
        seen = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(seen) == 1 << k

    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = 1 << k
        seen = [False] * cnt
        allOne = cnt - 1
        hashVal = 0
        for i in range(len(s)):
            hashVal = ((hashVal << 1) & allOne) | (int(s[i]))
            if i >= k - 1 and not seen[hashVal]:
                seen[hashVal] = True
                cnt -= 1
                if cnt == 0:
                    return True
        return False