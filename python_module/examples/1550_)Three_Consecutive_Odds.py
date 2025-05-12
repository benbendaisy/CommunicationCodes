class Solution:
    """
    Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.


    Example 1:

    Input: arr = [2,6,4,1]
    Output: false
    Explanation: There are no three consecutive odds.
    Example 2:

    Input: arr = [1,2,34,3,4,5,7,23,12]
    Output: true
    Explanation: [5,7,23] are three consecutive odds.
    """
    def threeConsecutiveOdds1(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        left, n = 0, len(arr)
        while left <= n - 3:
            if arr[left] % 2 == 1:
                if all(arr[left + i] % 2 == 1 for i in range(1, 3)):
                    return True
            left += 1
        return False
    
    def threeConsecutiveOdds2(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        cnt = 0
        for num in arr:
            if num % 2 == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False