class Solution:
    """
    You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.

    You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

    Return the maximum number of books you can take from the bookshelf.

    Example 1:

    Input: books = [8,5,2,7,9]
    Output: 19
    Explanation:
    - Take 1 book from shelf 1.
    - Take 2 books from shelf 2.
    - Take 7 books from shelf 3.
    - Take 9 books from shelf 4.
    You have taken 19 books, so return 19.
    It can be proven that 19 is the maximum number of books you can take.
    Example 2:

    Input: books = [7,0,3,4,5]
    Output: 12
    Explanation:
    - Take 3 books from shelf 2.
    - Take 4 books from shelf 3.
    - Take 5 books from shelf 4.
    You have taken 12 books so return 12.
    It can be proven that 12 is the maximum number of books you can take.
    Example 3:

    Input: books = [8,2,3,7,3,4,0,1,4,3]
    Output: 13
    Explanation:
    - Take 1 book from shelf 0.
    - Take 2 books from shelf 1.
    - Take 3 books from shelf 2.
    - Take 7 books from shelf 3.
    You have taken 13 books so return 13.
    It can be proven that 13 is the maximum number of books you can take.
    """
    def maximumBooks1(self, books: List[int]) -> int:
        def sum_valid_section(l, r):
            shelf_num = min(books[r], r - l + 1)
            return ((books[r] - (shelf_num - 1)) + books[r]) * shelf_num // 2
        n = len(books)
        mono_stack = []
        dp = [0] * n
        for i in range(n):
            while mono_stack and i - mono_stack[-1] > books[i] - books[mono_stack[-1]]:
                mono_stack.pop()
            if not mono_stack:
                dp[i] = sum_valid_section(0, i)
            else:
                dp[i] = sum_valid_section(mono_stack[-1] + 1, i) + dp[mono_stack[-1]]
            mono_stack.append(i)
        return max(dp)
    
    def maximumBooks2(self, books: List[int]) -> int:
        def sum_valid_section(l, r):
            shelf_num = min(books[r], r - l + 1)
            return ((books[r] - (shelf_num - 1)) + books[r]) * shelf_num // 2
        n = len(books)
        stack, dp = [], [0] * n
        for i in range(n):
            while stack and i - stack[-1] > books[i] - books[stack[-1]]:
                stack.pop()
            
            if not stack:
                dp[i] = sum_valid_section(0, i)
            else:
                dp[i] = sum_valid_section(stack[-1] + 1, i) + dp[stack[-1]]
            stack.append(i)
        return max(dp)
    
    def maximumBooks3(self, books: List[int]) -> int:
        n = len(books)

        # Helper function to calculate the sum of books in a given range [l, r]
        def calculateSum(l, r):
            cnt = min(books[r], r - l + 1)
            return (2 * books[r] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * n

        for i in range(n):
            # While we cannot push i, we pop from the stack
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            # Compute dp[i]
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)

            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum element in the dp array
        return max(dp)
    
    def maximumBooks4(self, books: List[int]) -> int:
        def cal_seq(l: int, r: int) -> int:
            shelf_num = min(books[r], r - l + 1)
            start_num = books[r] - (shelf_num - 1) # left num and right num is books[r]
            return (start_num + books[r]) * shelf_num // 2 # arithmetic sequence equals to (first + last) * n // 2
        n = len(books)
        stack, dp = [], [0] * n
        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] > books[i] - i:
                stack.pop()
            
            if not stack:
                dp[i] = cal_seq(0, i)
            else:
                dp[i] = cal_seq(stack[-1] + 1, i) + dp[stack[-1]]
            stack.append(i)
        return max(dp)