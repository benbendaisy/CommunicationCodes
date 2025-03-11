class Solution:
    """
    You are given a string word and a non-negative integer k.

    Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
    
    Example 1:

    Input: word = "aeioqq", k = 1

    Output: 0

    Explanation:

    There is no substring with every vowel.

    Example 2:

    Input: word = "aeiou", k = 0

    Output: 1

    Explanation:

    The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

    Example 3:

    Input: word = "ieaouqqieaouqq", k = 1

    Output: 3

    Explanation:

    The substrings with every vowel and one consonant are:

    word[0..5], which is "ieaouq".
    word[6..11], which is "qieaou".
    word[7..12], which is "ieaouq".
    """
    def countOfSubstrings1(self, word: str, k: int) -> int:
        """
        time limit exceeded
        """
        vowels = {"a", "e", "i", "o", "u"}
        n, cnt = len(word), 0
        for i in range(n):
            vowel_set = set()
            constant = 0
            for j in range(i, n):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                else:
                    constant += 1
                if len(vowel_set) == 5 and constant == k:
                    cnt += 1
        return cnt
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n, cnt = len(word), 0
        left = 0
        vowel_cnt = {v: 0 for v in vowels}
        constant = 0
        for right in range(n):
            ch = word[right]
            if ch in vowels:
                vowel_cnt[ch] += 1
            else:
                constant += 1

            while constant > k:
                left_char = word[left]
                if left_char in vowels:
                    vowel_cnt[left_char] -= 1
                else:
                    constant -= 1
                left += 1

            if constant == k and all(v >= 1 for _, v in vowel_cnt.items()):
                    cnt += 1
        return cnt
    
    def countOfSubstrings1(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)

        @lru_cache(None)
        def count_substrings(i: int, vowel_set: frozenset, constant: int) -> int:
            if i >= n:
                return 0
            new_vowel_set = vowel_set | {word[i]} if word[i] in vowels else vowel_set
            new_constant = constant + (word[i] not in vowels)

            # Check if this substring is valid
            valid_count = 1 if len(new_vowel_set) == 5 and new_constant == k else 0
            
            # Continue recursion
            return valid_count + count_substrings(i + 1, new_vowel_set, new_constant)

        total_count = sum(count_substrings(i, frozenset(), 0) for i in range(n))
        return total_count