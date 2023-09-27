from typing import List


class Solution:
    """
    There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute the candies to the children.

    Example 1:

    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    Example 2:

    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.
    """
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Initialize a list to store the number of candies for each child
        candies = [1] * n
        # First pass: Check ratings from left to right
        for i in range(1, n):
            if ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                # If the current child has a higher rating and fewer or equal candies than the previous child,
                # give them one more candy than the previous child
                candies[i] = candies[i - 1] + 1
        
        # Second pass: Check ratings from right to left
        for j in range(n - 2, -1, -1):
            if ratings[j + 1] < ratings[j] and candies[j + 1] >= candies[j]:
                candies[j] = candies[j + 1] + 1
        total = sum(candies)
        return total