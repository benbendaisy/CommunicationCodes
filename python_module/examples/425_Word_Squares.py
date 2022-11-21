from typing import List


class Solution:
    """
        Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

        A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

        For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

        Example 1:

        Input: words = ["area","lead","wall","lady","ball"]
        Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
        Explanation:
        The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
        Example 2:

        Input: words = ["abat","baba","atan","atal"]
        Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
        Explanation:
        The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
    """
    def wordSquares1(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        def get_words_with_prefix(prefix):
            for word in words:
                if word.startswith(prefix):
                    yield word

        def back_tracking(step, word_squares, results):
            if step == n:
                results.append(word_squares[:])
                return
            prefix = "".join([word[step] for word in word_squares])
            # find out all words that start with the given prefix
            for candidate in get_words_with_prefix(prefix):
                word_squares.append(candidate)
                back_tracking(step + 1, word_squares, results)
                word_squares.pop()

        results = []
        word_squares = []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            back_tracking(1, word_squares, results)
        return results

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        def build_trie():
            self.trie = {}
            for idx, word in enumerate(words):
                node = self.trie
                for char in word:
                    if char in node:
                        node = node[char]
                    else:
                        new_node = {}
                        new_node["#"] = []
                        node[char] = new_node
                        node = new_node
                    node["#"].append(idx)

        def get_words_with_prefix(prefix):
            node = self.trie
            for char in prefix:
                if char not in node:
                    return []
                node = node[char]
            return [words[idx] for idx in node["#"]]

        def back_tracking(step, word_squares, results):
            if step == n:
                results.append(word_squares[:])
                return

            prefix = "".join([word[step] for word in word_squares])
            for candidate in get_words_with_prefix(prefix):
                word_squares.append(candidate)
                back_tracking(step + 1, word_squares, results)
                word_squares.pop()

        build_trie()
        results = []
        word_square = []
        for word in words:
            word_square = [word]
            back_tracking(1, word_square, results)
        return results
