class Solution:
    """
    You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

    Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

    Example 1:

    Input: prob = [0.4], target = 1
    Output: 0.40000
    Example 2:

    Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
    Output: 0.03125
    

    Constraints:

    1 <= prob.length <= 1000
    0 <= prob[i] <= 1
    0 <= target <= prob.length
    Answers will be accepted as correct if they are within 10^-5 of the correct answer.
    """
    def probabilityOfHeads1(self, prob: List[float], target: int) -> float:
        n = len(prob)

        @cache
        def helper(idx: int, t: int):
            if t < 0:
                return 0.0
            
            if idx == n:
                return 1.0 if t == 0 else 0
            
            return prob[idx] * helper(idx + 1, t - 1) + (1 - prob[idx]) * helper(idx + 1, t)
        
        return helper(0, target)
    
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        if not prob:
            return 0.0
        
        n = len(prob)
        @cache
        def helper(idx: int, curr: int) -> float:
            if curr > target:
                return 0.0
            
            if idx == n:
                return 1.0 if curr == target else 0
            
            return prob[idx] * helper(idx + 1, curr + 1) + (1 - prob[idx]) * helper(idx + 1, curr)
        return helper(0, 0)