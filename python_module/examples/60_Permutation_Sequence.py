class Solution:
    """
    The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

    Example 1:

    Input: n = 3, k = 3
    Output: "213"
    Example 2:

    Input: n = 4, k = 9
    Output: "2314"
    Example 3:

    Input: n = 3, k = 1
    Output: "123"
    """
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        def back_track(path: list, choices: list):
            if len(res) >= k:
                return
            if not choices:
                if len(res) < k:
                    res.append(path)
                return
            for i in range(len(choices)):
                back_track(path + [choices[i]], choices[:i] + choices[i + 1:])
        
        back_track([], nums)
        return "".join(res[-1])