class Solution:
    """
    You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

    Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
    Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
    Return the lexicographically smallest string that can be written on the paper.

    Example 1:

    Input: s = "zza"
    Output: "azz"
    Explanation: Let p denote the written string.
    Initially p="", s="zza", t="".
    Perform first operation three times p="", s="", t="zza".
    Perform second operation three times p="azz", s="", t="".
    Example 2:

    Input: s = "bac"
    Output: "abc"
    Explanation: Let p denote the written string.
    Perform first operation twice p="", s="c", t="ba". 
    Perform second operation twice p="ab", s="c", t="". 
    Perform first operation p="ab", s="", t="c". 
    Perform second operation p="abc", s="", t="".
    Example 3:

    Input: s = "bdda"
    Output: "addb"
    Explanation: Let p denote the written string.
    Initially p="", s="bdda", t="".
    Perform first operation four times p="", s="", t="bdda".
    Perform second operation four times p="addb", s="", t="".
    """
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        t = []
        result = []
        min_char = 'a'

        for ch in s:
            t.append(ch)
            count[ch] -= 1

            # Update min_char to the smallest character left in s
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from t to result if it's <= smallest remaining in s
            while t and t[-1] <= min_char:
                result.append(t.pop())

        # Empty any remaining in t
        while t:
            result.append(t.pop())

        return ''.join(result)