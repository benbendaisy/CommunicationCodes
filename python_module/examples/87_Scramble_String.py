class Solution:
    """
    We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
    Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
    Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
    Apply step 1 recursively on each of the two substrings x and y.
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

    Example 1:

    Input: s1 = "great", s2 = "rgeat"
    Output: true
    Explanation: One possible scenario applied on s1 is:
    "great" --> "gr/eat" // divide at random index.
    "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
    "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
    "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
    "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
    "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
    The algorithm stops now, and the result string is "rgeat" which is s2.
    As one possible scenario led s1 to be scrambled to s2, we return true.
    Example 2:

    Input: s1 = "abcde", s2 = "caebd"
    Output: false
    Example 3:

    Input: s1 = "a", s2 = "a"
    Output: true
    """
    def isScramble1(self, s1: str, s2: str) -> bool:
        m = {}
        def helper(ss1, ss2):
            if (ss1, ss2) in m:
                return m[(ss1, ss2)]
            if not sorted(ss1) == sorted(ss2):
                return False
            if len(ss1) == 1:
                return True

            for i in range(1, len(ss1)):
                if helper(ss1[:i], ss2[-i:]) and helper(ss1[i:], ss2[:-i]) or helper(ss1[:i], ss2[:i]) and helper(ss1[i:], ss2[i:]):
                    m[(ss1, ss2)] = True
                    return True
            m[(ss1, ss2)] = False
            return False
        return helper(s1, s2)
    
    def isScramble2(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        
        if len(s1) != len(s2):
            return False
        
        if sorted(s1) != sorted(s2):
            return False

        @cache
        def helper(str1: str, str2: str):
            if str1 == str2:
                return True
            
            if sorted(str1) != sorted(str2):
                return False
            n = len(str1)
            for i in range(1, n):
                if helper(str1[:i], str2[:i]) and helper(str1[i:], str2[i:]):
                    return True
                
                if helper(str1[:i], str2[n - i:]) and helper(str1[i:], str2[:n - i]):
                    return True
            return False
        return helper(s1, s2)
    
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        
        if sorted(s1) != sorted(s2):
            return False
        
        @cache
        def helper(str1: str, str2: str):
            if str1 == str2:
                return True

            if sorted(str1) != sorted(str2):
                return False
            
            n = len(str1)
            for i in range(1, n):
                if helper(str1[:i], str2[:i]) and helper(str1[i:], str2[i:]):
                    return True
                
                if helper(str1[:i], str2[n - i:]) and helper(str1[i:], str2[:n - i]):
                    return True
            return False
        
        return helper(s1, s2)