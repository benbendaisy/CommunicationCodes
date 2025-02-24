from collections import Counter


class Solution:
    """
        Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

        Return the sorted string. If there are multiple answers, return any of them.

        Example 1:

        Input: s = "tree"
        Output: "eert"
        Explanation: 'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
        Example 2:

        Input: s = "cccaaa"
        Output: "aaaccc"
        Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
        Note that "cacaca" is incorrect, as the same characters must be together.
        Example 3:

        Input: s = "Aabb"
        Output: "bbAa"
        Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.
    """
    def frequencySort1(self, s: str) -> str:
        char_count_map = Counter(s)
        # sorted_char_count_map = {k: v for k, v in sorted(char_count_map.items(), key=lambda item: item[1], reverse=True)}
        sorted_char_count_map = dict(sorted(char_count_map.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key, value in sorted_char_count_map.items():
            res.extend([key] * value)
        return "".join(res)

    def frequencySort2(self, s: str) -> str:
        char_count_map = Counter(s)
        res = []
        for key, value in char_count_map.most_common():
            res.extend([key] * value)
        return "".join(res)
    
    def frequencySort3(self, s: str) -> str:
        cnts = Counter(s)
        str_builder = []
        for letter, freq in cnts.most_common():
            str_builder.append(letter * freq)
        return "".join(str_builder)
    
    def frequencySort(self, s: str) -> str:
        char_cnts = Counter(s)
        str_list = []
        for ch, cnt in char_cnts.most_common():
            str_list.append(ch * cnt)
        return "".join(str_list)