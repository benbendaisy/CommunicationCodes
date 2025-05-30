class WordDictionary1:
    """
        Design a data structure that supports adding new words and finding if a string matches any previously added string.

        Implement the WordDictionary class:

        WordDictionary() Initializes the object.
        void addWord(word) Adds word to the data structure, it can be matched later.
        bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

        Example:

        Input
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        Output
        [null,null,null,null,false,true,true,true]

        Explanation
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True
    """

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        trie = self.children
        for ch in word:
            trie = trie.setdefault(ch, {})
        trie["$"] = True

    def search(self, word: str) -> bool:
        def helper(trie, idx):
            if idx == len(word):
                return "$" in trie
            if word[idx] == ".":
                for ch in trie.keys():
                    if ch != "$" and helper(trie[ch], idx + 1):
                        return True
            if word[idx] in trie:
                return helper(trie[word[idx]], idx + 1)
            return False
        return helper(self.children, 0)

class WordDictionary2:
    class TrieNode:
        def __init__(self):
            self.child = {}
            self.is_ending = False
    def __init__(self):
        self.children = self.TrieNode()
    def addWord(self, word: str) -> None:
        node = self.children
        for ch in word:
            if ch not in node.child:
                node.child[ch] = self.TrieNode()
            node = node.child[ch]
        node.is_ending = True

    def search(self, word: str) -> bool:
        n = len(word)
        def helper(idx: int, node: self.TrieNode):
            if idx == n:
                return node.is_ending
            ch = word[idx]
            if ch == ".":
                return any(helper(idx + 1, child) for child in node.child.values())
            next_node = node.child.get(ch)
            return next_node is not None and helper(idx + 1, next_node)
        return helper(0, self.children)