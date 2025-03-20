class Solution:
    """
    Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

    All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

    Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

    Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.

    Example 1:

    Input: balls = [1,1]
    Output: 1.00000
    Explanation: Only 2 ways to divide the balls equally:
    - A ball of color 1 to box 1 and a ball of color 2 to box 2
    - A ball of color 2 to box 1 and a ball of color 1 to box 2
    In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
    Example 2:

    Input: balls = [2,1,1]
    Output: 0.66667
    Explanation: We have the set of balls [1, 1, 2, 3]
    This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equal probability (i.e. 1/12):
    [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
    After that, we add the first two balls to the first box and the second two balls to the second box.
    We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
    Probability is 8/12 = 0.66667
    Example 3:

    Input: balls = [1,2,1,2]
    Output: 0.60000
    Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
    Probability = 108 / 180 = 0.6
    """
    def getProbability1(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2  # Each box gets n balls

        @lru_cache(None)
        def dfs(index, count1, count2, distinct1, distinct2):
            """
            Recursively explore all ways to distribute balls.
            
            index     - Current color index being processed.
            count1    - Number of balls in box1.
            count2    - Number of balls in box2.
            distinct1 - Number of distinct colors in box1.
            distinct2 - Number of distinct colors in box2.
            """
            if count1 > n or count2 > n:
                return 0  # Invalid case: one box has too many balls
            
            if index == len(balls):  # Base case: all colors have been distributed
                return 1 if count1 == count2 and distinct1 == distinct2 else 0

            total_ways = 0  # Number of valid distributions
            color_count = balls[index]  # Number of balls of the current color
            
            # Try all possible ways to distribute these balls
            for i in range(color_count + 1):
                new_distinct1 = distinct1 + (1 if i > 0 else 0)
                new_distinct2 = distinct2 + (1 if (color_count - i) > 0 else 0)
                total_ways += comb(color_count, i) * dfs(index + 1, count1 + i, count2 + (color_count - i), new_distinct1, new_distinct2)

            return total_ways

        # Compute the total number of ways to distribute the balls
        total_ways = dfs(0, 0, 0, 0, 0)
        
        # Compute all possible distributions
        total_distributions = comb(total_balls, n)

        return total_ways / total_distributions
    
    def getProbability2(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2  # Each box gets exactly `n` balls

        @lru_cache(None)
        def dfs(index, count1, count2, distinct1, distinct2):
            """
            Recursively count valid distributions and total distributions.
            
            index     - Current color index being processed.
            count1    - Number of balls in box1.
            count2    - Number of balls in box2.
            distinct1 - Number of distinct colors in box1.
            distinct2 - Number of distinct colors in box2.
            """
            if count1 > n or count2 > n:
                return (0, 0)  # Invalid case, exceeds limit
            
            if index == len(balls):  # Base case: all colors processed
                return (1, 1) if count1 == count2 and distinct1 == distinct2 else (0, 1)

            valid_ways, total_ways = 0, 0
            color_count = balls[index]  # Number of balls of current color

            # Try distributing `i` balls to box1 and the rest to box2
            for i in range(color_count + 1):
                new_distinct1 = distinct1 + (1 if i > 0 else 0)
                new_distinct2 = distinct2 + (1 if (color_count - i) > 0 else 0)

                valid, total = dfs(index + 1, count1 + i, count2 + (color_count - i), new_distinct1, new_distinct2)
                
                # Multiply by the ways to choose `i` balls out of `color_count`
                coefficient = comb(color_count, i)
                valid_ways += valid * coefficient
                total_ways += total * coefficient

            return valid_ways, total_ways

        # Run recursive DFS
        valid_ways, total_ways = dfs(0, 0, 0, 0, 0)
        
        return valid_ways / total_ways
    
    def getProbability(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2
        m = len(balls)
        def helper(idx: int, cnt1: int, cnt2: int, distinct1: int, distinct2: int) -> int:
            if cnt1 > n or cnt2 > n:
                return (0, 0)
            
            if idx == m:
                return (1, 1) if cnt1 == cnt2 and distinct1 == distinct2 else (0, 1)
            
            valid_ways, total_ways = 0, 0
            color_cnt = balls[idx]

            for i in range(color_cnt + 1):
                # split i balls to box1 and color_cnt - i balls to box2
                new_distinct1 = distinct1 + (1 if i > 0 else 0)
                new_distinct2 = distinct2 + (1 if (color_cnt - i) > 0 else 0)
            
                valid, total = helper(idx + 1, cnt1 + i, cnt2 + color_cnt - i, new_distinct1, new_distinct2)
                # 
                coefficient = comb(color_cnt, i)
                valid_ways += valid * coefficient
                total_ways += total * coefficient
            return valid_ways, total_ways
        
        valid_ways, total_ways = helper(0, 0, 0, 0, 0)
        return valid_ways / total_ways