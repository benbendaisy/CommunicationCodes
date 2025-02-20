class Solution:
    """
    A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

    Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

    Example 1:

    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
    Example 2:

    Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    Output: 1859
    Example 3:

    Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    Output: 3086
    """
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        @cache
        def back_track(idx: int, cost: int, a_trip: int):
            if idx == len(costs):
                if a_trip == (len(costs) // 2):
                    return cost
                return float("inf")
            if a_trip > (len(costs) // 2):
                return float("inf")
            first = back_track(idx + 1, cost + costs[idx][0], a_trip + 1)
            second = back_track(idx + 1, cost + costs[idx][1], a_trip)
            return min(first, second)
        return back_track(0, 0, 0)
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2  # Total number of people per city
        
        @lru_cache(None)  # Memoization to avoid recomputation
        def backtrack(idx, countA, countB):
            # Base case: If we have assigned all people
            if idx == len(costs):
                return 0 if countA == countB == n else float('inf')
            if countA > n or countB > n:
                return float('inf')
            # Try sending person `idx` to City A or City B

            # Option 1: Send to City A (if we have slots left)
            cost_A = costs[idx][0] + backtrack(idx + 1, countA + 1, countB)

            # Option 2: Send to City B (if we have slots left)
            cost_B = costs[idx][1] + backtrack(idx + 1, countA, countB + 1)
                

            # Return the minimum of both choices
            return min(cost_A, cost_B)

        # Start recursion from index 0 with 0 people in each city
        return backtrack(0, 0, 0)