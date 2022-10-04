from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, val):
        curr = self.head
        for c in val:
            curr = curr.children[c]
        curr.end = True

    def printAll(self, curr, string, res):
        if(curr.end):
            res.append(string)
        for c in curr.children:
            string += c
            self.printAll(curr.children[c], string, res)
            string = string[:-1]

    def printMe(self):
        res = []
        self.printAll(self.head, '', res)
        return res