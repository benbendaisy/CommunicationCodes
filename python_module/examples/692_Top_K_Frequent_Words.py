import heapq
from collections import Counter
from typing import List


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    """
        Given an array of strings words and an integer k, return the k most frequent strings.

        Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

        Example 1:

        Input: words = ["i","love","leetcode","i","love","coding"], k = 2
        Output: ["i","love"]
        Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
        Example 2:

        Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
        Output: ["the","is","sunny","day"]
        Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
    """
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        if len(words) < k:
            return words
        wordCounter = Counter(words)
        return sorted(list(wordCounter.keys()), key=lambda x: (-wordCounter[x], x))[:k]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        if len(words) < k:
            return []

        wordCounter = Counter(words)
        heap = []
        for word, freq in wordCounter.items():
            heapq.heappush(heap, Pair(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p.word for p in sorted(heap, reverse=True)]
    
    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        # Count word frequencies
        freq = Counter(words)
        # Sort by frequency (descending) and then by word (ascending)
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        # Use a min-heap to get top k frequent words with correct ordering
        sorted_words = [word for word, _ in sorted_items]
        return sorted_words[:k]
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count word frequencies
        freq = Counter(words)
        
        # Use a min-heap to get top k frequent words with correct ordering
        return [word for word, _ in heapq.nsmallest(k, freq.items(), key=lambda x: (-x[1], x[0]))]
