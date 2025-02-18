class Solution:
    """
    You have n  tiles, where each tile has one letter tiles[i] printed on it.

    Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

    Example 1:

    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    Example 2:

    Input: tiles = "AAABBC"
    Output: 188
    Example 3:

    Input: tiles = "V"
    Output: 1
    """
    def numTilePossibilities1(self, tiles: str) -> int:
        @cache
        def back_track(av_chars):
            used = set()
            seqs = 0
            for i, ch in enumerate(av_chars):
                if ch in used:
                    continue
                used.add(ch)
                seqs += 1 + back_track(av_chars[:i] + av_chars[i + 1:])
            return seqs
        return back_track(tiles)
    
    def numTilePossibilities2(self, tiles: str) -> int:
        def backtrack(path, used):
            if path:  # Add the current permutation if it's not empty
                result.add("".join(path))
            for i in range(len(tiles)):  # Iterate through all characters
                if not used[i]:  # Skip if the character is already used
                    used[i] = True  # Mark the character as used
                    backtrack(path + [tiles[i]], used)  # Recurse with the updated path
                    used[i] = False  # Backtrack: unmark the character

        result = set()  # Use a set to avoid duplicates
        used = [False] * len(tiles)  # Track which characters have been used
        backtrack([], used)  # Start the backtracking process
        return len(result)

    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(path, choices):
            if path:
                result.add(path)
            if not choices:
                return
            for i in range(len(choices)):  # Iterate through all characters
                backtrack(path + choices[i], choices[:i] + choices[i + 1:])
        result = set()
        backtrack("", tiles)
        return len(result)
