class Solution:
    """
    You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

    Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

    Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

    Return the selected subsequence. If there are multiple answers, return any of them.

    Note: The elements in words are distinct.

    Example 1:

    Input: words = ["e","a","b"], groups = [0,0,1]

    Output: ["e","b"]

    Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

    Example 2:

    Input: words = ["a","b","c","d"], groups = [1,0,1,1]

    Output: ["a","b","c"]

    Explanation: A subsequence that can be selected is ["a","b","c"] because groups[0] != groups[1] and groups[1] != groups[2]. Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3]. It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.
    """
    def getLongestSubsequence1(self, words: List[str], groups: List[int]) -> List[str]:
        if not words or not groups:
            return []
        
        res, n = [], len(words)
        @cache
        def helper(idx: int, path: tuple):
            nonlocal res
            if idx == n:
                if len(path) > len(res):
                    res = [words[i] for i in path]
                return
            
            if not path or groups[path[-1]] != groups[idx]:
                helper(idx + 1, path + (idx, ))
            else:
                helper(idx + 1, path)
        
        helper(0, ())
        return res
    
    def getLongestSubsequence2(self, words: List[str], groups: List[int]) -> List[str]:
        if not words or not groups:
            return []
        
        n = len(words)
        @cache
        def helper(idx: int, last_group: int):
            if idx == n:
                return ()
            
            # option 1: take the current
            take = ()
            if last_group != groups[idx]:
                next_take = helper(idx + 1, groups[idx])
                take = (idx, ) + next_take
            else:
                # option 2: skip the current
                take = helper(idx + 1, last_group)

            return take
        
        return [words[i] for i in helper(0, -1)]
        
    
    def getLongestSubsequence3(self, words: List[str], groups: List[int]) -> List[str]:
        if not words or not groups:
            return []
        
        n = len(words)
        @cache
        def helper(idx: int, last_group: int):
            if idx == n:
                return ()
            
            # option 1: take the current
            take = ()
            if last_group != groups[idx]:
                next_take = helper(idx + 1, groups[idx])
                take = (idx, ) + next_take
            
            # option 2: skip the current
            skip = helper(idx + 1, last_group)

            return skip if len(skip) > len(take) else take
        
        return [words[i] for i in helper(0, -1)]