class Solution:
    """
    Given a string s consisting only of characters a, b and c.

    Return the number of substrings containing at least one occurrence of all these characters a, b and c.

    Example 1:

    Input: s = "abcabc"
    Output: 10
    Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
    Example 2:

    Input: s = "aaacb"
    Output: 3
    Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
    Example 3:

    Input: s = "abc"
    Output: 1
    """
    def numberOfSubstrings1(self, s: str) -> int:
        """
        Time Limit Exceeded
        """
        def check(str1: str) -> bool:
            for ch in ("a", "b", "c"):
                if ch not in str1:
                    return False
            return True
        n, cnt = len(s), 0
        for i in range(n):
            for j in range(i, n):
                if check(s[i:j + 1]):
                    cnt += 1
        return cnt
    
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }  # Store the count of 'a', 'b', and 'c'
        left, total = 0, 0
        
        for right in range(len(s)):
            count[s[right]] += 1  # Expand the window by adding s[right]
            
            while all(count[ch] > 0 for ch in "abc"):  # If the window is valid
                total += len(s) - right  # Add all valid substrings
                count[s[left]] -= 1  # Shrink from the left
                left += 1
                
        return total