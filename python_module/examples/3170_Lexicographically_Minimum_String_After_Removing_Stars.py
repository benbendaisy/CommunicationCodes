class Solution:
    """
    You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

    While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
    Return the lexicographically smallest resulting string after removing all '*' characters.

    Example 1:

    Input: s = "aaba*"

    Output: "aab"

    Explanation:

    We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

    Example 2:

    Input: s = "abc"

    Output: "abc"

    Explanation:

    There is no '*' in the string.
    """
    def clearStars1(self, s: str) -> str:
        """
        Removes stars from a string by deleting the smallest character to the left.
        
        A star (*) removes the smallest lexicographical non-star character to its left.
        If there are ties for the smallest character, it removes the one that is
        closest to the star (i.e., the rightmost one).

        Args:
            s: The input string with lowercase letters and stars.

        Returns:
            The resulting string after all stars have been processed.
        """
        if not s:
            return ""

        # A min-heap to efficiently find the smallest character.
        # We store tuples of (character, -original_index).
        # The negative index is a trick to handle the tie-breaking rule:
        # for the same character, the one with a larger index (further right)
        # will have a smaller negative index, so it will be prioritized by the min-heap.
        min_heap = []

        # A set to keep track of the indices of characters that have been removed.
        deleted_indices = set()

        # First pass: identify which characters to delete
        for i, char in enumerate(s):
            if char == '*':
                # If there are characters to remove, pop the smallest one from the heap.
                if min_heap:
                    # Pop the smallest char (and its rightmost index in case of a tie)
                    # The original index is stored as a negative, so we negate it back.
                    _, neg_index = heapq.heappop(min_heap)
                    deleted_indices.add(-neg_index)
            else:
                # Add the character and its location to the heap.
                heapq.heappush(min_heap, (char, -i))

        # Second pass: build the final string
        result = []
        for i, char in enumerate(s):
            # Skip stars and characters whose indices were marked for deletion.
            if char == '*' or i in deleted_indices:
                continue
            result.append(char)
            
        return "".join(result)
    
    def clearStars2(self, s: str) -> str:
        if not s:
            return ""

        min_heap, del_indices = [], set()
        for i, ch in enumerate(s):
            if ch == '*':
                if min_heap:
                    _, neg_idx = heapq.heappop(min_heap)
                    del_indices.add(-neg_idx)
            else:
                heapq.heappush(min_heap, (ch, -i))
        
        arr = []
        for i, ch in enumerate(s):
            if ch == '*' or i in del_indices:
                continue
            arr.append(ch)
        return "".join(arr)