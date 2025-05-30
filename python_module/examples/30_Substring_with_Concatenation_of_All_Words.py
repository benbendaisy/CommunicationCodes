import collections
from typing import List


class Solution:
    """
        You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

        You can return the answer in any order.

        Example 1:

        Input: s = "barfoothefoobarman", words = ["foo","bar"]
        Output: [0,9]
        Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.
        Example 2:

        Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
        Output: []
        Example 3:

        Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
        Output: [6,9,12]

        Constraints:

        1 <= s.length <= 104
        1 <= words.length <= 5000
        1 <= words[i].length <= 30
        s and words[i] consist of lowercase English letters.
    """
    def findSubstring0(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer

    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j : j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer
    
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        
        result = []
        
        for i in range(word_len):  # Shift window starting point
            left = i
            right = i
            window_words = Counter()
            count = 0  # Count of valid words in the window
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    window_words[word] += 1
                    count += 1
                    
                    while window_words[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        window_words[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        result.append(left)
                else:
                    window_words.clear()
                    count = 0
                    left = right
        
        return result
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_cnt = len(words)
        freq = Counter(words)

        res = []
        for i in range(word_len):
            left, right = i, i
            window_words = Counter()
            cnt = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in freq:
                    window_words[word] += 1
                    cnt += 1
                    while window_words[word] > freq[word]:
                        left_word = s[left:left + word_len]
                        window_words[left_word] -= 1
                        cnt -= 1
                        left += word_len
                    if cnt == word_cnt:
                        res.append(left)
                else:
                    window_words.clear()
                    cnt = 0
                    left = right
        return res