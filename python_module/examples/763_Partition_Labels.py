class Solution:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

    Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

    Return a list of integers representing the size of these parts.

    Example 1:

    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
    Example 2:

    Input: s = "eccbbbbdec"
    Output: [10]
    """
    def partitionLabels1(self, s: str) -> List[int]:
        if not s:
            return []
        n = len(s)
    
        def helper(idx: int, path: list[int], visited: set) -> list[int]:
            if idx == n:
                return path
            
            for i in range(idx, n):
                sub = s[idx:i + 1]
                if all(ch not in visited for ch in sub):
                    visited.update(list(sub))
                    res = helper(i + 1, path + [len(sub)], visited)
                    if res:
                        return res
                    visited.difference_update(list(sub))
            return []
        visited = set()
        return helper(0, [], visited)

    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Precompute the last occurrence of each character
        last_occurrence = {ch: i for i, ch in enumerate(s)}

        def helper(idx: int) -> List[int]:
            if idx >= len(s):
                return []

            end = last_occurrence[s[idx]]  # Determine the partition end
            i = idx

            # Expand the partition to cover all characters within it
            while i <= end:
                end = max(end, last_occurrence[s[i]])
                i += 1  # Move to the next character

            # Recursively call for the remaining part of the string
            return [end - idx + 1] + helper(end + 1)

        return helper(0)