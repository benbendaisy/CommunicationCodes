class Solution:
    """
    Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

    Return the number of positive integers that can be generated that are less than or equal to a given integer n.

    Example 1:

    Input: digits = ["1","3","5","7"], n = 100
    Output: 20
    Explanation: 
    The 20 numbers that can be written are:
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
    Example 2:

    Input: digits = ["1","4","9"], n = 1000000000
    Output: 29523
    Explanation: 
    We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
    81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
    2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
    In total, this is 29523 integers that can be written using the digits array.
    Example 3:

    Input: digits = ["7"], n = 8
    Output: 1
    """
    def atMostNGivenDigitSet1(self, digits: List[str], n: int) -> int:
        if not digits or n <= 0:
            return 0
        
        m = len(digits)
        visited = set()
        @cache
        def helper(path: str):
            if path:
                if int(path) <= n:
                    visited.add(path)
                else:
                    return
            
            for num in digits:
                helper(path + str(num))
        helper("")
        return len(visited)
    
    def atMostNGivenDigitSet2(self, digits: List[str], n: int) -> int:
        str_n = str(n)
        d_len = len(digits)
        n_len = len(str_n)

        # Count numbers with fewer digits than n
        count = sum(d_len ** i for i in range(1, n_len))

        @cache
        def dfs(idx: int, is_prefix_limited: bool) -> int:
            """Counts valid numbers recursively."""
            if idx == n_len:
                return 1  # Reached valid number

            total = 0
            for digit in digits:
                if is_prefix_limited and digit > str_n[idx]:
                    continue  # Prune invalid paths
                
                total += dfs(idx + 1, is_prefix_limited and digit == str_n[idx])

            return total

        # Count numbers with the same number of digits as n
        count += dfs(0, True)
        return count
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_n = str(n)
        len_n = len(str_n)
        d_len = len(digits)

        cnt = sum(d_len ** i for i in range(1, len_n))

        @cache
        def helper(idx: int, is_prefix_limit: bool) -> int:
            if idx == len_n:
                return 1
            
            total = 0
            for digit in digits:
                if is_prefix_limit and digit > str_n[idx]:
                    continue
                total += helper(idx + 1, is_prefix_limit and digit == str_n[idx])
            return total
        
        cnt += helper(0, True)
        return cnt