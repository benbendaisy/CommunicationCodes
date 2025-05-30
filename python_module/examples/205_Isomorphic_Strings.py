class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

    Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Example 2:

    Input: s = "foo", t = "bar"
    Output: false
    Example 3:

    Input: s = "paper", t = "title"
    Output: true
    """
    def isIsomorphic1(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        return True
    
    def isIsomorphic2(self, s: str, t: str) -> bool:
        def transform_string(str1):
            index_map = {}
            new_str = []
            for i, c in enumerate(str1):
                if c not in index_map:
                    index_map[c] = i
                new_str.append(str(index_map[c]))
            return " ".join(new_str)
        return transform_string(s) == transform_string(t)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(str1: str):
            idx_dict = {}
            new_str = []
            for ch in str1:
                if ch not in idx_dict:
                    idx_dict[ch] = len(idx_dict) + 1
                new_str.append(str(idx_dict[ch]))
            return "".join(new_str)
        return transform(s) == transform(t)

