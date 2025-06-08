from typing import List

from examples.TrieTree import Trie


class Solution:
    """
        Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

        You must write an algorithm that runs in O(n) time and uses O(1) extra space.

        Example 1:

        Input: n = 13
        Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
        Example 2:

        Input: n = 2
        Output: [1,2]

        Constraints:

        1 <= n <= 5 * 104
    """
    def lexicalOrder1(self, n: int) -> List[int]:
        """
        time complexity: o(nlogn)
        :param n:
        :return:
        """
        arr = [x for x in range(1, n + 1)]
        arr.sort(key=lambda x: str(x))
        return arr

    def lexicalOrder2(self, n: int) -> List[int]:
        """
        O(9n) => O(n) solution
        :param n:
        :return:
        """
        res = []
        def dfs(num):
            res.append(num)
            for i in range(10):
                newNum = num * 10 + i
                if newNum > n:
                    break
                dfs(newNum)
        if n < 10:
            return [x for x in range(1, n + 1)]
        else:
            for i in range(1, 10):
                dfs(i)
        return res

    def lexicalOrder3(self, n: int) -> List[int]:
        """
        O(9n) => O(n) solution
        :param n:
        :return:
        """
        t = Trie()
        for i in range(1, n+1):
            t.add(str(i))
        return([int(c) for c in t.printMe()])

    def lexicalOrder4(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1

        # Generate numbers from 1 to n
        for _ in range(n):
            lexicographical_numbers.append(current_number)

            # If multiplying the current number by 10 is within the limit, do it
            if current_number * 10 <= n:
                current_number *= 10
            else:
                # Adjust the current number by moving up one digit
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10  # Remove the last digit
                current_number += 1  # Increment the number

        return lexicographical_numbers

