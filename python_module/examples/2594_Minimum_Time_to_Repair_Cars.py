class Solution:
    """
    You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

    You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

    Return the minimum time taken to repair all the cars.

    Note: All the mechanics can repair the cars simultaneously.

    Example 1:

    Input: ranks = [4,2,3,1], cars = 10
    Output: 16
    Explanation: 
    - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
    - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
    - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
    - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
    Example 2:

    Input: ranks = [5,1,8], cars = 6
    Output: 16
    Explanation: 
    - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
    - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
    """
    def repairCars1(self, ranks: List[int], cars: int) -> int:
        if not ranks or cars <= 0:
            return 0
        n = len(ranks)
        ranks.sort()
        @cache
        def helper(idx: int, remainings: int, max_time):
            if remainings == 0:
                return max_time
            if idx == n:
                return float("inf")
            
            min_time = float('inf')
            for i in range(remainings, -1, -1):
                fix_time = ranks[idx] * i * i
                min_time = min(min_time, helper(idx + 1, remainings - i, max(fix_time, max_time)))
            return min_time
        max_time = helper(0, cars, float('-inf'))
        return max_time if max_time != float('inf') else 0
    
    def repairCars2(self, ranks: List[int], cars: int) -> int:
        ranks.sort()

        # Helper function to check if we can repair `cars` within `time` limit
        def canRepairInTime(time):
            total_cars = 0
            for rank in ranks:
                total_cars += int((time // rank) ** 0.5)  # max cars a mechanic can fix
                if total_cars >= cars:  # Stop early if we reach the target
                    return True
            return total_cars >= cars

        # Binary search for the minimum required time
        left, right = 0, ranks[0] * (cars ** 2)  # Upper bound
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
        
        return left  # Minimum required time
    
    def repairCars3(self, ranks: List[int], cars: int) -> int:
        ranks.sort()

        def is_valid(time: int) -> bool:
            total = 0
            for rank in ranks:
                total += int((time / rank) ** 0.5)
                if total >= cars:
                    return True
            return False
        
        left, right = 1, ranks[0] * (cars ** 2)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()

        def is_valid(time: int) -> bool:
            cnt = 0
            for rank in ranks:
                cnt += int((time // rank) ** 0.5)
                if cnt >= cars:
                    return True
            return False
        
        left, right = 1, ranks[0] * cars ** 2
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left