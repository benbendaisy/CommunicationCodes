class Solution:
    """
    Given an array of integers cost and an integer target, return the maximum integer you can paint under the following rules:

    The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
    The total cost used must be equal to target.
    The integer does not have 0 digits.
    Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".

    Example 1:

    Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
    Output: "7772"
    Explanation: The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
    Digit    cost
    1  ->   4
    2  ->   3
    3  ->   2
    4  ->   5
    5  ->   6
    6  ->   7
    7  ->   2
    8  ->   5
    9  ->   5
    Example 2:

    Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
    Output: "85"
    Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
    """
    def largestNumber(self, cost: List[int], target: int) -> str:
        if not cost:
            return ""
        
        n = len(cost)
        @cache
        def helper(path: str, running_costs: int) -> int:
            if running_costs == target:
                return int(path)
            
            max_num = float('-inf')
            for i in range(1, n + 1):
                t = running_costs + cost[i - 1]
                if t <= target:
                    max_num = max(max_num, helper(path + str(i), t))
            return max_num

        return str(helper("", 0)) if helper("", 0) != float('-inf') else "0"
    
    def largestNumber(self, cost: List[int], target: int) -> str:
        if not cost or target == 0:
            return "0" # Base case: exact match

        n = len(cost)
        @cache
        def helper(remaining: int):
            if remaining == 0:
                return ""
            
            max_num = "0" # Default smallest value (invalid case)
            for i in range(1, n + 1): # Iterate from largest to smallest digit
                new_cost = remaining - cost[i - 1]
                if new_cost >= 0:
                    candidate = helper(new_cost)
                    if candidate != "0": # Ensure we only take valid numbers
                        max_num = max(max_num, candidate + str(i), key=lambda x: (len(x), x))
            return max_num
        return helper(target)