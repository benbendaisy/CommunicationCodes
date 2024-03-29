import collections
from collections import Counter
from typing import List


class Solution:
    """
        You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

        You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

        You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
        Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
        Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
        Given the integer array fruits, return the maximum number of fruits you can pick.

        Example 1:

        Input: fruits = [1,2,1]
        Output: 3
        Explanation: We can pick from all 3 trees.
        Example 2:

        Input: fruits = [0,1,2,2]
        Output: 3
        Explanation: We can pick from trees [1,2,2].
        If we had started at the first tree, we would only pick from trees [0,1].
        Example 3:

        Input: fruits = [1,2,3,2,2]
        Output: 4
        Explanation: We can pick from trees [2,3,2,2].
        If we had started at the first tree, we would only pick from trees [1,2].
    """
    def totalFruit1(self, fruits: List[int]) -> int:
        MAX_BASKETS = 2
        fruit_counter = Counter()
        output, w_start = 0, 0
        for f in fruits:
            # if current fruit is not in the basket and the size of baskets is two
            if fruit_counter[f] == 0 and len(fruit_counter) == MAX_BASKETS:
                # shrink the window to contain one type of fruits
                while len(fruit_counter) >= MAX_BASKETS:
                    x = fruits[w_start]
                    fruit_counter[x] -= 1
                    if fruit_counter[x] == 0:
                        fruit_counter.pop(x)
                    w_start += 1
            # add current fruit to the basket
            fruit_counter[f] += 1
            output = max(output, fruit_counter.total())
        return output

    def totalFruit(self, fruits: List[int]) -> int:
        """
            Given an array tree of integers representing types of fruit in a basket,
            the goal is to find the length of the longest contiguous subarray where
            at most two types of fruit are present.
        :param fruits:
        :return:
        """
        ans = 0
        count_dict = collections.defaultdict(int)

        # running window with size 2
        l = 0
        for r, t in enumerate(fruits):
            count_dict[t] += 1
            while len(count_dict) > 2:
                count_dict[fruits[l]] -= 1
                if count_dict[fruits[l]] == 0:
                    del count_dict[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
