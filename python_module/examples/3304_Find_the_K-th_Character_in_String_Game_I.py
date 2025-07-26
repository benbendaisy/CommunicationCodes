class Solution:
    """
    Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
    For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

    Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

    Note that the character 'z' can be changed to 'a' in the operation.

    Example 1:

    Input: k = 5

    Output: "b"

    Explanation:

    Initially, word = "a". We need to do the operation three times:

    Generated string is "b", word becomes "ab".
    Generated string is "bc", word becomes "abbc".
    Generated string is "bccd", word becomes "abbcbccd".
    Example 2:

    Input: k = 10

    Output: "c"
    """
    def kthCharacter(self, k: int) -> str:
        char_dict = {
            'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i',
            'i': 'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q',
            'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y',
            'y':'z', 'z':'a'
        }

        s = 'a'
        while len(s) < k:
            new_s = s
            for ch in s:
                new_s += char_dict[ch]
            s = new_s
        return s[k - 1]