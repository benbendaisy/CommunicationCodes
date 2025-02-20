class Solution:
    """
    We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
    Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

    Example 1:

    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1: 0
    Example 2:

    Input: n = 2, k = 1
    Output: 0
    Explanation: 
    row 1: 0
    row 2: 01
    Example 3:

    Input: n = 2, k = 2
    Output: 1
    Explanation: 
    row 1: 0
    row 2: 01
    """
    def kthGrammar1(self, n: int, k: int) -> int:
        def helper(n1, k1, root_val):
            if n1 == 1:
                return root_val
            total_nodes = 2 ** (n1 - 1)
            if k1 > (total_nodes / 2):
                next_root_val = 1 if root_val == 0 else 0
                return helper(n1 - 1, k1 - (total_nodes / 2), next_root_val)
            else:
                next_root_val = 0 if root_val == 0 else 1
                return helper(n1 - 1, k1, next_root_val)
        return helper(n, k, 0)
    
    def kthGrammar2(self, n: int, k: int) -> int:
        def helper(n1, k1):
            if n1 == 1:
                return 0
            total_elements = 2 ** (n1 - 1)
            half_elements = total_elements // 2
            if k1 > half_elements:
                return 1 - helper(n1, k1 - half_elements)
            return helper(n1 - 1, k1)
        return helper(n, k)
    
    def kthGrammar3(self, n: int, k: int) -> int:
        @cache
        def helper(m):
            if m == 1:
                return [0]
            prev = helper(m - 1)
            res = []
            for e in prev:
                if e == 0:
                    res.extend([0,1])
                elif e == 1:
                    res.extend([1, 0])
                else:
                    res.append(e)
            return res
        return helper(n)[k - 1]
    
    def kthGrammar(self, n: int, k: int) -> int:
        @cache
        def helper(n1, k1):
            if n1 == 1:
                return 0
            if k1 % 2 == 1:
                return helper(n1 - 1, (k1 + 1) // 2)
            return abs(1 - helper(n1 - 1, k1 // 2))
        return helper(n, k)