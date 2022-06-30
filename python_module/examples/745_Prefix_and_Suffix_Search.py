import collections
from typing import List
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie1 = Trie()

    def f(self, prefix: str, suffix: str) -> int:
        return -1