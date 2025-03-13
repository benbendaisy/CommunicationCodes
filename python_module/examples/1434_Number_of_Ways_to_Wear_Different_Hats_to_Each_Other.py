class Solution:
    """
    There are n people and 40 types of hats labeled from 1 to 40.

    Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.

    Return the number of ways that n people can wear different hats from each other.

    Since the answer may be too large, return it modulo 109 + 7.

    Example 1:

    Input: hats = [[3,4],[4,5],[5]]
    Output: 1
    Explanation: There is only one way to choose hats given the conditions. 
    First person choose hat 3, Second person choose hat 4 and last one hat 5.
    Example 2:

    Input: hats = [[3,5,1],[3,5]]
    Output: 4
    Explanation: There are 4 ways to choose hats:
    (3,5), (5,3), (1,3) and (1,5)
    Example 3:

    Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    Output: 24
    Explanation: Each person can choose hats labeled from 1 to 4.
    Number of Permutations of (1,2,3,4) = 24.
    """
    def numberWays1(self, hats: List[List[int]]) -> int:
        if not hats:
            return 0
        
        n = len(hats)
        @cache
        def helper(idx: int, path: tuple):
            if idx == n:
                return 1
            
            ways = 0
            path = set(path)
            for i in range(len(hats[idx])):
                if hats[idx][i] not in path:
                    path.add(hats[idx][i])
                    ways += helper(idx + 1, tuple(path))
                    path.remove(hats[idx][i])
            return ways
        return helper(0, ())
    
    def numberWays2(self, hats: List[List[int]]) -> int:
        if not hats:
            return 0
        n = len(hats)
        max_mask = (1 << n) - 1
        @cache
        def helper(idx: int, mask):
            if idx == n:
                return 1
            
            ways = 0
            for hat in hats[idx]:
                if (1 << hat) & mask == 0:
                    new_mask = mask | (1 << hat)
                    ways += helper(idx + 1, new_mask)
            return ways
        
        return helper(0, 0)
    
    def numberWays3(self, hats: List[List[int]]) -> int:
        if not hats:
            return 0
        
        n = len(hats)  # Number of people
        MOD = 10**9 + 7  # Common modulo for coding problems
        
        # Create a mapping of hat to people who can wear it
        # This is the key optimization - we iterate through hats rather than people
        hat_to_people = [[] for _ in range(41)]  # Max hat number is 40 as per constraints
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_people[hat].append(person)
        
        # Use a mask to track which people have been assigned hats
        @cache
        def dp(hat_idx: int, people_mask: int) -> int:
            # If all people have hats, we found a valid assignment
            if people_mask == (1 << n) - 1:
                return 1
            
            # If we've gone through all possible hats but not all people have hats
            if hat_idx > 40:
                return 0
            
            # Skip this hat
            ways = dp(hat_idx + 1, people_mask) % MOD
            
            # Try assigning this hat to each person who can wear it
            for person in hat_to_people[hat_idx]:
                # If this person doesn't have a hat yet
                if not (people_mask & (1 << person)):
                    # Assign the hat to this person
                    ways = (ways + dp(hat_idx + 1, people_mask | (1 << person))) % MOD
            
            return ways
        
        return dp(1, 0)  # Start with hat 1 and no people assigned