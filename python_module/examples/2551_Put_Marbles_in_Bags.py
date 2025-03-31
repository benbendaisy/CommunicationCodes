from typing import List


class Solution:
    """
    You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

    Divide the marbles into the k bags according to the following rules:

    No bag is empty.
    If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
    If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
    The score after distributing the marbles is the sum of the costs of all the k bags.

    Return the difference between the maximum and minimum scores among marble distributions.

    Example 1:

    Input: weights = [1,3,5,1], k = 2
    Output: 4
    Explanation: 
    The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
    The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
    Thus, we return their difference 10 - 6 = 4.
    Example 2:

    Input: weights = [1, 3], k = 2
    Output: 0
    Explanation: The only distribution possible is [1],[3]. 
    Since both the maximal and minimal score are the same, we return 0.
    """
    def putMarbles1(self, weights: List[int], k: int) -> int:
        v = []
        n = len(weights)
        for i in range(n - 1):
            v.append(weights[i] + weights[i + 1])
        v.sort()
        return sum(v[n - k:]) - sum(v[:k - 1])
    
    def putMarbles2(self, weights: List[int], k: int) -> int:
        self.min_score = float('inf')
        self.max_score = float('-inf')
        n = len(weights)

        @cache
        def helper(idx: int, p: int, running_score: int):
            if p == k - 1:  # Last partition takes the remaining elements
                partition_score = running_score + weights[idx] + weights[-1]
                self.min_score = min(self.min_score, partition_score)
                self.max_score = max(self.max_score, partition_score)
                return
            
            for i in range(idx, n - 1):  # Try different partition points
                partition_score = running_score + weights[idx] + weights[i]
                helper(i + 1, p + 1, partition_score)

        helper(0, 0, 0)
        return self.max_score - self.min_score

    def putMarbles3(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0  # Only one way to partition, so min and max scores are the same.

        # Compute pairwise sums of consecutive elements
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]

        # Sort the pair sums to determine best and worst partitions
        pair_sums.sort()

        # The min score uses the smallest (k-1) pairs, max score uses the largest (k-1) pairs
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        return max_score - min_score
    
    def putMarbles4(self, weights: List[int], k: int) -> int:
        if not weights:
            return 0
        n = len(weights)
        if k == 1:
            return 0
        sums = []
        for i in range(n - 1):
            sums.append(weights[i] + weights[i + 1])
        sums.sort()
        return sum(sums[-(k-1):]) - sum(sums[:k - 1])