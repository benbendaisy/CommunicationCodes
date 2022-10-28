from collections import Counter, defaultdict


class Solution:
    """
        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.

        A substring is a contiguous sequence of characters within the string.

        Example 1:

        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
        Example 2:

        Input: s = "a", t = "a"
        Output: "a"
        Explanation: The entire string s is the minimum window.
        Example 3:

        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.
    """
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dictT = Counter(t)
        # Number of unique characters in t, which need to be present in the desired window.
        requiredLength = len(dictT)
        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        dictWindow = defaultdict(lambda : 0)
        ans = (float('inf'), None, None)
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            dictWindow[character] += 1
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dictT and dictWindow[character] == dictT[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == requiredLength:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                dictWindow[character] -= 1
                if character in dictT and dictWindow[character] < dictT[character]:
                    formed -= 1
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]




