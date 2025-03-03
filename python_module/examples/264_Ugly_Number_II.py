class Solution:
    """
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return the nth ugly number.



    Example 1:

    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    Example 2:

    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    """
    def nthUglyNumber1(self, n: int) -> int:
        def isUglyNumber(k: int):
            if k < 1:
                return False

            for i in [2, 3, 5]:
                while k % i == 0:
                    k /= i
                if k == 1:
                    return True
            return False

        idx = 1
        while n > 0:
            if isUglyNumber(idx):
                n -= 1
            if n == 0:
                return idx
            idx += 1

    def nthUglyNumber2(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))

        return ugly[-1]
    
    def nthUglyNumber3(self, n: int) -> int:
        seen = {1}
        heap = [1]

        @cache
        def helper(cnt: int):
            if cnt == n:
                return heapq.heappop(heap)
            
            ugly = heapq.heappop(heap)
            for f in (2, 3, 5):
                new_num = f * ugly
                if new_num not in seen:
                    seen.add(new_num)
                    heapq.heappush(heap, new_num)
            return helper(cnt + 1)
        
        return helper(1)
    
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        ugly = [1]
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1

            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]