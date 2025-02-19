class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = min([len(s) for s in strs])
        for i in range(min_length):
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    return strs[j - 1][:i]
        return strs[0][:min_length]

    def longestCommonPrefix(self, strs: List[str]) -> str:
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