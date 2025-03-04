class Solution:
    """
    There is a test that has n types of questions. You are given an integer target and a 0-indexed 2D integer array types where types[i] = [counti, marksi] indicates that there are counti questions of the ith type, and each one of them is worth marksi points.

    Return the number of ways you can earn exactly target points in the exam. Since the answer may be too large, return it modulo 109 + 7.

    Note that questions of the same type are indistinguishable.

    For example, if there are 3 questions of the same type, then solving the 1st and 2nd questions is the same as solving the 1st and 3rd questions, or the 2nd and 3rd questions.

    Example 1:

    Input: target = 6, types = [[6,1],[3,2],[2,3]]
    Output: 7
    Explanation: You can earn 6 points in one of the seven ways:
    - Solve 6 questions of the 0th type: 1 + 1 + 1 + 1 + 1 + 1 = 6
    - Solve 4 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 1 + 2 = 6
    - Solve 2 questions of the 0th type and 2 questions of the 1st type: 1 + 1 + 2 + 2 = 6
    - Solve 3 questions of the 0th type and 1 question of the 2nd type: 1 + 1 + 1 + 3 = 6
    - Solve 1 question of the 0th type, 1 question of the 1st type and 1 question of the 2nd type: 1 + 2 + 3 = 6
    - Solve 3 questions of the 1st type: 2 + 2 + 2 = 6
    - Solve 2 questions of the 2nd type: 3 + 3 = 6
    Example 2:

    Input: target = 5, types = [[50,1],[50,2],[50,5]]
    Output: 4
    Explanation: You can earn 5 points in one of the four ways:
    - Solve 5 questions of the 0th type: 1 + 1 + 1 + 1 + 1 = 5
    - Solve 3 questions of the 0th type and 1 question of the 1st type: 1 + 1 + 1 + 2 = 5
    - Solve 1 questions of the 0th type and 2 questions of the 1st type: 1 + 2 + 2 = 5
    - Solve 1 question of the 2nd type: 5
    Example 3:

    Input: target = 18, types = [[6,1],[3,2],[2,3]]
    Output: 1
    Explanation: You can only earn 18 points by answering all questions.
    """
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        if not types:
            return 0
        mod = 10 ** 9 + 7
        n = len(types)
        @cache
        def helper(idx: int, running_sum: int) -> int:
            if running_sum == target:
                return 1 # Found a valid way to reach the target
            
            if idx == n:
                return 0 # No more types left or exceeded target

            ways = 0
            cnt, mark = types[idx]
            for i in range(cnt + 1): # Try using 0 to max_count of this type
                t = running_sum + mark * i
                if t <= target:
                    ways += helper(idx + 1, t)
            return ways
        
        return helper(0, 0) % mod






