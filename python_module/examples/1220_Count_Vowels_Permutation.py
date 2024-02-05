from functools import lru_cache


class Solution:
    """
        Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        Since the answer may be too large, return it modulo 10^9 + 7.

        Example 1:

        Input: n = 1
        Output: 5
        Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
        Example 2:

        Input: n = 2
        Output: 10
        Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
        Example 3:

        Input: n = 5
        Output: 68

        Constraints:

        1 <= n <= 2 * 10^4
    """
    def countVowelPermutation1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def vowel_permutation_count(i, vowel):
            total = 1
            if i > 1:
                if vowel == 'a':
                    total = (vowel_permutation_count(i - 1, 'e') + vowel_permutation_count(i - 1, 'i') + vowel_permutation_count(i - 1, 'u')) % MOD
                elif vowel == 'e':
                    total = (vowel_permutation_count(i - 1, 'a') + vowel_permutation_count(i - 1, 'i')) % MOD
                elif vowel == 'i':
                    total = (vowel_permutation_count(i - 1, 'e') + vowel_permutation_count(i - 1, 'o')) % MOD
                elif vowel == 'o':
                    total = vowel_permutation_count(i - 1, 'i')
                else:
                    total = (vowel_permutation_count(i - 1, 'i') + vowel_permutation_count(i - 1, 'o')) % MOD
            return total

        return sum(vowel_permutation_count(n, vowel) for vowel in 'aeiou') % MOD

    def countVowelPermutation2(self, n: int) -> int:
        # initialize the number of strings ending with a, e, i, o, u
        a_count = e_count = i_count = o_count = u_count = 1
        MOD = 10 ** 9 + 7

        for i in range(1, n):
            a_count_new = (e_count + i_count + u_count) % MOD
            e_count_new = (a_count + i_count) % MOD
            i_count_new = (e_count + o_count) % MOD
            o_count_new = (i_count) % MOD
            u_count_new = (i_count + o_count) % MOD

            # https://docs.python.org/3/reference/expressions.html#evaluation-order
            a_count, e_count, i_count, o_count, u_count = \
                a_count_new, e_count_new, i_count_new, o_count_new, u_count_new

        return (a_count + e_count + i_count + o_count + u_count) % MOD

    def countVowelPermutation3(self, n: int) -> int:

        a_vowel_permutation_count = [1] * n
        e_vowel_permutation_count = [1] * n
        i_vowel_permutation_count = [1] * n
        o_vowel_permutation_count = [1] * n
        u_vowel_permutation_count = [1] * n

        MOD = 10 ** 9 + 7

        for i in range(1, n):
            a_vowel_permutation_count[i] = (e_vowel_permutation_count[i - 1] + i_vowel_permutation_count[i - 1] + u_vowel_permutation_count[i - 1]) % MOD
            e_vowel_permutation_count[i] = (a_vowel_permutation_count[i - 1] + i_vowel_permutation_count[i - 1]) % MOD
            i_vowel_permutation_count[i] = (e_vowel_permutation_count[i - 1] + o_vowel_permutation_count[i - 1]) % MOD
            o_vowel_permutation_count[i] = (i_vowel_permutation_count[i - 1]) % MOD
            u_vowel_permutation_count[i] = (i_vowel_permutation_count[i - 1] + o_vowel_permutation_count[i - 1]) % MOD

        result = 0

        result = (a_vowel_permutation_count[n - 1] + e_vowel_permutation_count[n - 1] + \
                  i_vowel_permutation_count[n - 1] + o_vowel_permutation_count[n - 1] + \
                  u_vowel_permutation_count[n - 1]) % MOD

        return result
    
    def countVowelPermutation4(self, n: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def vowel_permutation(i, vowel):
            total = 1
            if i > 1:
                if vowel == 'a':
                    total = (vowel_permutation(i - 1, 'e') + vowel_permutation(i - 1, 'i') + vowel_permutation(i - 1, 'u')) % mod
                elif vowel == 'e':
                    total = (vowel_permutation(i - 1, 'a') + vowel_permutation(i - 1, 'i')) % mod
                elif vowel == 'i':
                    total = (vowel_permutation(i - 1, 'e') + vowel_permutation(i - 1, 'o')) % mod
                elif vowel == 'o':
                    total = vowel_permutation(i - 1, 'i')
                else:
                    total = (vowel_permutation(i - 1, 'i') + vowel_permutation(i - 1, 'o')) % mod
            return total
        return sum(vowel_permutation(n, vowel) for vowel in 'aeiou') % mod