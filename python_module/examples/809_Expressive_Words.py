from collections import Counter
from typing import List


class Solution:
    """
    Sometimes people repeat letters to represent extra feeling. For example:

    "hello" -> "heeellooo"
    "hi" -> "hiiii"
    In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

    You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
    Return the number of query strings that are stretchy.

    Example 1:

    Input: s = "heeellooo", words = ["hello", "hi", "helo"]
    Output: 1
    Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
    Example 2:

    Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
    Output: 3
    """
    def expressiveWords1(self, s: str, words: List[str]) -> int:
        f = lambda x: (tuple(zip(*[(k, len(tuple(g))) for k, g in groupby(x)])))
        (sch, sct), ans = f(s), 0
        for word in words:
            wch, wct = f(word)
            if sch == wch:
                for sc, wc in zip(sct, wct):
                    if sc < wc or (sc < 3 and sc != wc):
                        break
                else:
                    ans += 1
        return ans

    # def expressiveWords(self, s: str, words: List[str]) -> int:
    #     def get_counter(x: str):
    #         char_counter = Counter(x)
    #         return dict(sorted(char_counter.items(), key = lambda i: i[0]))
    #
    #     s_counter = get_counter(s)
    #     ans = 0
    #     for word in words:
    #         word_counter = get_counter(word)
    #         if s_counter.keys() == word_counter.keys():
    #             for sc, wc in zip(s_counter.values(), word_counter.values()):
    #                 if sc < wc or (sc < 3 and sc != wc):
    #                     break
    #                 else:
    #                     ans += 1
    #     return ans
