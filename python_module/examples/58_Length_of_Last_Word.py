class Solution:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal 
    substring
    consisting of non-space characters only.

    Example 1:

    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.
    Example 2:

    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.
    Example 3:

    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.
    """
    def lengthOfLastWord1(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        words = s.strip().split(" ")
        last_word = words[-1].strip()
        return len(last_word)
    
    def lengthOfLastWord3(self, s: str) -> int:
        if not s:
            return 0
        p = len(s) - 1
        while p >= 0 and s[p] == " ":
            p -= 1
        
        length = 0
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1
        return length