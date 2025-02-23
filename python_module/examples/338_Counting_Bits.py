from typing import List


class Solution:
    """
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

        Example 1:

        Input: n = 2
        Output: [0,1,1]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        Example 2:

        Input: n = 5
        Output: [0,1,1,2,1,2]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101

        Constraints:

        0 <= n <= 105

    """
    def countBits1(self, n: int) -> List[int]:
        if n < 0:
            return []
        res = [0]
        def count_one(num):
            cnt = 0
            while num > 0:
                if num & 1 == 1:
                    cnt += 1
                num >>= 1
            return cnt
        for i in range(1, n + 1):
            cnt = count_one(i)
            res.append(cnt)
        return res
    
    def countBits(self, n: int) -> list[int]:
        """
        Returns an array where ans[i] is the number of 1's in the binary representation of i.
        Uses dynamic programming with the observation that for any number x, 
        number of 1's in x equals number of 1's in (x & (x-1)) plus 1.
        
        Args:
            n: Upper bound of the range [0, n]
            
        Returns:
            List where ans[i] contains number of 1's in binary representation of i
        
        Time complexity: O(n)
        Space complexity: O(n) for the output array
        """
        # Initialize array with 0's
        ans = [0] * (n + 1)
        
        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            # For any number i, number of 1's equals
            # number of 1's in (i & (i-1)) plus 1
            # i & (i-1) removes the rightmost 1 in binary representation of i
            ans[i] = ans[i & (i-1)] + 1
            
        return ans