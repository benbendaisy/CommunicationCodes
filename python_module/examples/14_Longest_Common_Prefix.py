class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    """
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = min([len(s) for s in strs])
        for i in range(min_length):
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    return strs[j - 1][:i]
        return strs[0][:min_length]

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        class TreeNode:
            def __init__(self):
                self.child = {}
                self.cnt = 0
                self.is_end = False
        
        class TrieTree:
            def __init__(self):
                self.root = TreeNode()
                self.min_length = 0
            
            def insert(self, word: str):
                self.min_length = min(self.min_length, len(word))
                node = self.root
                for ch in word:
                    if ch not in node.child:
                        node.child[ch] = TreeNode()
                    node = node.child[ch]
                    node.cnt += 1
                node.is_end = True
            
            def longest_prefix(self):
                node = self.root
                prefix = ""
                level = 0
                while node and len(node.child) == 1 and not node.is_end:
                    ch = next(iter(node.child))
                    prefix += ch
                    node = node.child[ch]
                return prefix
            
        if not strs:
            return ""
        trie = TrieTree()
        for word in strs:
            trie.insert(word)
        return trie.longest_prefix()
    
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(min(strs, key=len))
        res = ""
        for i in range(length):
            new_res = res + strs[0][i]
            for word in strs:
                if word[i] != new_res[i]:
                    return res
            res = new_res
        return res
    
    def longestCommonPrefix4(self, strs: List[str]) -> str:
        if not strs:
            return 0
        n = len(strs)
        min_length = len(min(strs, key=len))
        prefix = ""
        for i in range(min_length):
            ch = strs[0][i]
            for word in strs:
                if word[i] != ch:
                    return prefix
            prefix += ch
        return prefix
    
    def longestCommonPrefix5(self, strs: List[str]) -> str:
        if not strs:
            return 0
        m = len(strs)
        n = min(len(str1) for str1 in strs)
        pre_fix = ""
        for i in range(1, n + 1):
            pre_fix = strs[0][:i]
            for j in range(m):
                if strs[j][:i] != pre_fix:
                    return pre_fix[:-1]
        return pre_fix
    
    def longestCommonPrefix6(self, strs: List[str]) -> str:
        if not strs:
            return 0
        m = len(strs)
        n = min(len(str1) for str1 in strs)
        pre_fix = ""
        for i in range(n):
            new_str = pre_fix + strs[0][i]
            for word in strs:
                if word[i] != new_str[i]:
                    return pre_fix
            pre_fix = new_str
        return pre_fix
