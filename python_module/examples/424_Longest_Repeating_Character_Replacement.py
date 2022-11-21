class Solution:
    """
        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above operations.

        Example 1:

        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.
        Example 2:

        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        def is_window_valid(start, end, count):
            return end + 1 - start - count <= k

        all_letters = set(s)
        max_length = 0
        # iterate over each unique letter
        for letter in all_letters:
            start, cnt = 0, 0

            # initialize a sliding window for each unique letter
            for end in range(len(s)):
                if s[end] == letter:
                    # if the letter matches, increase the count
                    cnt += 1
                # bring start forward until the window is valid again
                while not is_window_valid(start, end, cnt):
                    if s[start] == letter:
                        # if the letter matches, decrease the count
                        cnt -= 1
                    start += 1

                # at this point the window is valid, update max_length
                max_length = max(max_length, end + 1 - start)
        return max_length
