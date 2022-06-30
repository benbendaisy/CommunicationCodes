from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self):
        self.children = defaultdict(lambda : TreeNode())
        self.words = []
class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.words.append(word)

    def search(self, word: str):
        node = self.root
        for ch in word:
            if not node.children[ch]:
                return False
            node = node.children[ch]

        return node.words



class Solution:
    """
        You are given an array of strings products and a string searchWord.

        Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

        Return a list of lists of the suggested products after each character of searchWord is typed.

        Example 1:

        Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
        Output: [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
        ]
        Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
        After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
        After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
        Example 2:

        Input: products = ["havana"], searchWord = "havana"
        Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        Example 3:

        Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
        Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

        Constraints:

        1 <= products.length <= 1000
        1 <= products[i].length <= 3000
        1 <= sum(products[i].length) <= 2 * 104
        All the strings of products are unique.
        products[i] consists of lowercase English letters.
        1 <= searchWord.length <= 1000
        searchWord consists of lowercase English letters.
    """
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggestions, ans = defaultdict(list), []

        for p in sorted(products):
            for i in range(1,len(p)+1):
                if len(suggestions[p[:i]]) < 3: suggestions[p[:i]].append(p)

        for i in range(1,len(searchWord)+1):
            ans.append(suggestions[searchWord[:i]])
        return ans

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)

        res = []
        for i in range(len(searchWord)):
            t = root.search(searchWord[:i + 1])
            if t:
                res.append(sorted(t)[:3])
            else:
                res.append([])
        return res