import math
from collections import Counter
from typing import List


class Solution:
    """
        You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

        Return the minimum number of transactions required to settle the debt.

        Example 1:

        Input: transactions = [[0,1,10],[2,0,5]]
        Output: 2
        Explanation:
        Person #0 gave person #1 $10.
        Person #2 gave person #0 $5.
        Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
        Example 2:

        Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
        Output: 1
        Explanation:
        Person #0 gave person #1 $10.
        Person #1 gave person #0 $1.
        Person #1 gave person #2 $5.
        Person #2 gave person #0 $5.
        Therefore, person #1 only need to give person #0 $4, and all debt is settled.
    """
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # - Any unsettled balances between n people can be resolved in at most n-1 transactions.
        # - The number of transations possible between n people is ~ n^2.
        # - So we try out all the possible ways to pick at most n-1 transations from the n^2 available
        # - Note that this sounds like the total possibilities are ~ O(n^2 CHOOSE n)
        #   but as noted below, once we pick a transaction, we remove all other transactions that
        #   include the originating node of the transaction since we don't want to any loops (Creating a loop with n-1 transations will lead to unsettled debts).
        # - Essentially this means that the first level of recursion has n - 1 choices, second level has n - 2 and so on

        # - Each transaction we pick settles the balance of at most 2 people
        # - We prune the search by not picking transactions that don't settle the balance of anyone
        #   eg transation between someone who is settled and and an unsettled person
        # - Another way to prune is not to settle between person of same sign since at best it will not improve
        #   on optimal solution and at worst will be sub optimal
        def back_track(arr, idx):
            if idx == len(arr):
                return 0
            if not arr[idx]:
                return back_track(arr, idx + 1)

            min_tractions = math.inf
            for i in range(idx + 1, len(arr)):
                if arr[i] * arr[idx] < 0:
                    arr[i] += arr[idx]
                    min_tractions = min(1 + back_track(arr, idx + 1), min_tractions)
                    arr[i] -= arr[idx]
            return min_tractions

        balance = Counter()
        # Calculates the net balance amt each person should receive or give
        for from_, to, amt in transactions:
            balance[to] += amt
            balance[from_] -= amt
        balance = list(balance.values())
        return back_track(balance, 0)