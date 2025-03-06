class Solution:
    """
    In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

    You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

    You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

    Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

    Example 1:

    Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
    Output: 14
    Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
    In special offer 1, you can pay $5 for 3A and 0B
    In special offer 2, you can pay $10 for 1A and 2B. 
    You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
    Example 2:

    Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
    Output: 11
    Explanation: The price of A is $2, and $3 for B, $4 for C. 
    You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
    You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
    You cannot add more items, though only $9 for 2A ,2B and 1C.
    """
    def shoppingOffers0(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        this is a backtracking problem with brute force solution
        got TLE
        """
        if not price or not needs:
            return 0
        
        n = len(special)
        def helper(bought: list[int], running_cost: int) -> int:
            if bought == needs:
                return running_cost
            
            min_cost = running_cost
            # if do not use any special offer
            for i in range(len(bought)):
                if needs[i] < bought[i]:
                    return float('inf')
                min_cost += price[i] * (needs[i] - bought[i])

            for i in range(0, n):
                # if take the special offer
                for j in range(len(special[i]) - 1):
                    bought[j] += special[i][j]
                min_cost = min(min_cost, helper(bought, running_cost + special[i][-1]))
                # setting the bought back
                for j in range(len(special[i]) - 1):
                    bought[j] -= special[i][j]
            
            return min_cost
        
        bought = [0] * len(needs)
        res = helper(bought, 0)
        return -1 if res == float('inf') else res
    
    def shoppingOffers1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not price or not needs:
            return 0
        
        n = len(needs)
        # Filter out invalid special offers (which exceed needs)
        valid_offers = []
        for offer in special:
            if all(offer[i] <= needs[i] for i in range(n)):
                valid_offers.append(offer)
        
        @cache
        def helper(remaining: tuple) -> int:
            # If needs are all zero, cost is 0
            if all(x == 0 for x in remaining):
                return 0
            
            # Compute the cost without using any special offers (greedy approach)
            min_cost = sum(price[i] * remaining[i] for i in range(n))
            # Try using each valid special offer
            for offer in valid_offers:
                new_needs = tuple(remaining[i] - offer[i] for i in range(n))
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + helper(new_needs))
            return min_cost
        
        return helper(tuple(needs))
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not special:
            return -1
        
        valid_offers = []
        n = len(needs)
        for offer in special:
            if all(offer[i] <= needs[i] for i in range(n)):
                valid_offers.append(offer)
        
        @cache
        def helper(remainings: tuple):
            if all(x == 0 for x in remainings):
                return 0
           
            min_cost = sum(price[i] * remainings[i] for i in range(n))
            for offer in special:
                new_needs = [remainings[i] - offer[i] for i in range(n)]
                if all(new_needs[i] >= 0 for i in range(n)):
                    min_cost = min(min_cost, offer[-1] + helper(tuple(new_needs)))
            return min_cost
        
        return helper(tuple(needs))