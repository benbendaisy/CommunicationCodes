from collections import Counter


class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window
    substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

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
    def minWindow1(self, s: str, t: str) -> str:
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

    def minWindow2(self, s: str, t: str) -> str:
        """
        1, two dict: dict_t and dict_window
        2, two lengths: one required length and the length of window that only includes characters in target string
        3, 3.1: adding the character to the window, 3.2: checking if need to adjust the length of window
           3.3: shrink the window
        """
        if not s or not t:
            return ""
        dict_t = Counter(t)
        req_length = len(dict_t)
        l, r = 0, 0
        formed = 0
        dict_window = defaultdict(lambda: 0)
        res = (float('inf'), None, None)
        while r < len(s):
            ch = s[r]
            dict_window[ch] += 1
            if ch in dict_t and dict_window[ch] == dict_t[ch]:
                formed += 1
            while l <= r and formed == req_length:
                character = s[l]
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                dict_window[character] -= 1
                if character in dict_t and dict_window[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]
    
    def minWindow3(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        freq1 = Counter(t)
        m = len(s)
        freq2 = defaultdict(int)
        left, min_str = 0, ""
        formed_chars, required_chars = 0, len(freq1)
        min_len = float('inf')
        for i in range(m):
            ch = s[i]
            if ch in freq1:
                freq2[ch] += 1
                if freq2[ch] == freq1[ch]:
                    formed_chars += 1 
            while formed_chars == required_chars:
                if i - left + 1 < min_len:
                    min_len = i - left + 1
                    min_str = s[left: i + 1]
                
                if s[left] in freq1:
                    freq2[s[left]] -= 1
                    if freq2[s[left]] < freq1[s[left]]:
                        formed_chars -= 1
                left += 1

        return min_str