from typing import List


class Solution:
    """
    Given an integer array arr of distinct integers and an integer k.

    A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

    Return the integer which will win the game.

    It is guaranteed that there will be a winner of the game.

    Example 1:

    Input: arr = [2,1,3,5,4,6,7], k = 2
    Output: 5
    Explanation: Let's see the rounds of the game:
    Round |       arr       | winner | win_count
    1   | [2,1,3,5,4,6,7] | 2      | 1
    2   | [2,3,5,4,6,7,1] | 3      | 1
    3   | [3,5,4,6,7,1,2] | 5      | 1
    4   | [5,4,6,7,1,2,3] | 5      | 2
    So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
    Example 2:

    Input: arr = [3,2,1], k = 10
    Output: 3
    Explanation: 3 will win the first 10 rounds consecutively.
    """
    def getWinner1(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        que = deque(arr[1:])
        curr = arr[0]
        win_streak = 0
        while que:
            oppo = que.popleft()
            if curr > oppo:
                que.append(oppo)
                win_streak += 1
            else:
                que.append(curr)
                curr = oppo
                win_streak = 1
            if win_streak == k or curr == max_element:
                return curr
        return -1
    
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        cur = arr[0]
        win_streak = 0
        for i in range(1, len(arr)):
            oppo = arr[i]
            if cur > oppo:
                win_streak += 1
            else:
                cur = oppo
                win_streak = 1
            if win_streak == k or cur == max_element:
                return cur
        return -1