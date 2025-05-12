class Solution:
    """
    You are given an integer array digits, where each element is a digit. The array may contain duplicates.

    You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.
    For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

    Return a sorted array of the unique integers.

    Example 1:

    Input: digits = [2,1,3,0]
    Output: [102,120,130,132,210,230,302,310,312,320]
    Explanation: All the possible integers that follow the requirements are in the output array. 
    Notice that there are no odd integers or integers with leading zeros.
    Example 2:

    Input: digits = [2,2,8,8,2]
    Output: [222,228,282,288,822,828,882]
    Explanation: The same digit can be used as many times as it appears in digits. 
    In this example, the digit 8 is used twice each time in 288, 828, and 882. 
    Example 3:

    Input: digits = [3,7,5]
    Output: []
    Explanation: No even integers can be formed using the given digits.
    """
    def findEvenNumbers1(self, digits: List[int]) -> List[int]:
        if not digits or len(digits) < 3:
            return []
        digits.sort()
        res, n = set(), len(digits)
        @cache
        def helper(path: tuple, candidates):
            if path and path[0] == 0:
                return
            if len(path) == 3:
                # path = tuple(sorted(path))
                res.add(path)
                return
            
            if not candidates:
                return
            
            for i in range(len(candidates)):
                helper(path + (candidates[i],), candidates[:i] + candidates[i + 1:])
        
        helper((), tuple(digits))
        res = [int("".join(list(map(str, lst)))) for lst in res]
        res = [num for num in res if num % 2 == 0]
        res.sort()
        return res
    
    def findEvenNumbers2(self, digits: List[int]) -> List[int]:
        res = set()

        def helper(path):
            if len(path) == 3:
                num = int("".join(map(str, path)))
                if num % 2 == 0:
                    res.add(num)
                return

            for i in range(len(digits)):
                if used[i]:
                    continue
                # Skip leading zero
                if len(path) == 0 and digits[i] == 0:
                    continue
                # Avoid duplicates: skip same digit at same level
                if i > 0 and digits[i] == digits[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                helper(path + [digits[i]])
                used[i] = False
        used = [False] * len(digits)
        digits.sort()
        helper([])
        return sorted(res)
    
    def findEvenNumbers3(self, digits: List[int]) -> List[int]:
        res = set()
        @cache
        def helper(path):
            if len(path) == 3:
                num = int("".join(map(str, list(path))))
                if num % 2 == 0:
                    res.add(num)
                return

            for i in range(len(digits)):
                if used[i]:
                    continue
                # Skip leading zero
                if len(path) == 0 and digits[i] == 0:
                    continue
                # Avoid duplicates: skip same digit at same level
                if i > 0 and digits[i] == digits[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                helper(path + (digits[i],))
                used[i] = False
        used = [False] * len(digits)
        digits.sort()
        helper(())
        return sorted(res)
    
    def findEvenNumbers4(self, digits: List[int]) -> List[int]:
        res, n = set(), len(digits)
        @cache
        def helper(path: tuple) -> None:
            if len(path) == 3:
                num = int("".join(map(str, list(path))))
                if num % 2 == 0:
                    res.add(num)
                return
            
            for i in range(n):
                if used[i] or (len(path) == 0 and digits[i] == 0):
                    continue
                
                used[i] = True
                helper(path + (digits[i],))
                used[i] = False
        
        used = [False] * n
        helper(())
        return sorted(res)